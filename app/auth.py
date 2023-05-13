from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .bdd.models import User
from .bdd import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('singup.html')


@auth.route('/signup', methods=['POST', 'GET'])
def signup_post():
    dni = request.form.get('dni')
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    #tipo = request.form.get('tipo')
    #sucursal = request.form.get('sucursal')
    password = request.form.get('password')

    if (dni == "" or nombre == "" or email == "" or password == ""):
        flash('Por favor, complete correctamente todos los datos')
        return redirect(url_for('auth.signup'))

    if (dni != "" and nombre != "" and email != "" and password != ""):
        user = User.query.filter_by(dniUser=dni).first()

        if user:  # Si el usuario existe, vuelve a la pagina de registro
            flash('Numero de Dni existente')
            return redirect(url_for('auth.signup'))

        else:  # crear un nuevo usuario con los datos ingresados.
            new_user = User(dniUser=dni, nombreUser=nombre, emailUser=email,
                            passwordUser=generate_password_hash(password,
                                                                method='sha256'))

            # agregar un nuevo usuario a la base de datos
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario agregado correctamente')

            return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    dni = request.form.get('dni')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    if dni == "":
        flash('Por favor, ingrese un Dni')
        return redirect(url_for('auth.login'))

    else:

        user = User.query.filter_by(dniUser=dni).first()
        # verificar si el dni de usuarioo email existe

        # comparar el hash del usuario y comparar con el hash de la base de datos
        if not user or not check_password_hash(user.passwordUser, password):
            flash('Por favor, verifique su Dni, password e ingreselo nuevamente')
            # si el usuario no existe o el password esta mal, recargar la pagina
            return redirect(url_for('auth.login'))

        # si verifica el hash, entonces las credenciales son correctas
        login_user(user, remember=remember)

        return redirect(url_for('profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
