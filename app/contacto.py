from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Contacto
from .bdd import db


contacto2 = Blueprint('contacto', __name__)


@contacto2.route('/contacto')
def contacto():
    return render_template('contacto.html')


@contacto2.route('/contacto', methods=['POST', 'GET'])
def contacto_post():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    consulta = request.form.get('consulta')

    if email == "":
        flash('Por favor, ingrese su mail y envíe su consulta')
        return redirect(url_for('contacto.contacto'))

    if email != "":
        # if this returns a user, then the email already exists in database
        user = Contacto.query.filter_by(emailContacto=email).first()

    if user:
        flash('Usted ya realizó una consulta. Por favor, espere la respuesta')
        return redirect(url_for('contacto.contacto'))

    new_user = Contacto(nombreContacto=nombre,
                        emailContacto=email, consultaContacto=consulta)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('contacto.consultaenviada'))


@contacto2.route('/consultaenviada')
def consultaenviada():
    return render_template('consultaenviada.html')
