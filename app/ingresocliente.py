from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Cliente, db

ingresocliente2 = Blueprint('inscliente', __name__)


@ingresocliente2.route('/inscliente')
def inscliente():
    return render_template('ingresocliente.html')


@ingresocliente2.route('/inscliente', methods=['POST', 'GET'])
def inscliente_post():
    dni = request.form.get('dni')
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    direccion = request.form.get('direccion')
    sucursal = request.form.get('sucursal')
    nivel = request.form.get('nivel')

    cliente = Cliente.query.filter_by(dniCliente=dni).first()

    if cliente:
        flash('Cliente existente en la base de datos')
        return redirect(url_for('inscliente.inscliente'))

    if not cliente:
        clienteagregar = Cliente(
                    nombreCliente=nombre, dniCliente=dni, emailCliente=email,
                    direccionCliente=direccion, sucursalCliente=sucursal,
                    nivelCliente=nivel)

        db.session.add(clienteagregar)
        db.session.commit()
        flash('Cliente agregado')
        return redirect(url_for('inscliente.inscliente'))

        if clienteagregar:
            flash('Cliente existente')
            return redirect(url_for('inscliente.inscliente'))
