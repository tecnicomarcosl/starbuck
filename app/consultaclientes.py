from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Cliente


conscliente2 = Blueprint('conscliente', __name__)
clientestodos2 = Blueprint('clientestodos', __name__)


@clientestodos2.route('/clientestodos')
def clientestodos():
    nombreconsulta = Cliente.query.all()
    cantidad = Cliente.query.count()
    flash('clientes existentes para la consulta realizada')
    return render_template('mostrarconsultaclientes.html',
                           nombre=nombreconsulta, cantidad=cantidad)


@conscliente2.route('/conscliente')
def conscliente():
    return render_template('consultacliente.html')


@conscliente2.route('/conscliente', methods=['POST', 'GET'])
def conscliente_post():
    codigo = request.form.get('codigo')
    dni = request.form.get('dni')
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    direccion = request.form.get('direccion')
    sucursal = request.form.get('sucursal')
    nivel = request.form.get('nivel')

    if (codigo == "" and dni == "" and nombre == "" and email == ""
            and direccion == "" and sucursal == "Sucursal del Cliente"
            and nivel == ""):
        flash('Por favor, complete algún parámetro para la busqueda')
        return redirect(url_for('conscliente.conscliente'))

    elif codigo != "":
        codigoconsulta = Cliente.query.filter_by(idCliente=codigo).all()

        if not codigoconsulta:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if codigoconsulta:
            cantidad = Cliente.query.filter_by(idCliente=codigo).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=codigoconsulta, cantidad=cantidad)

    elif dni != "":
        dniconsulta = Cliente.query.filter_by(dniCliente=dni).all()

        if not dniconsulta:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if dniconsulta:
            cantidad = Cliente.query.filter_by(dniCliente=dni).count()
            flash('cliente existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=dniconsulta, cantidad=cantidad)

    elif nombre != "":
        nombreconsulta = Cliente.query.filter_by(nombreCliente=nombre).all()

        if not nombreconsulta:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if nombreconsulta:
            cantidad = Cliente.query.filter_by(nombreCliente=nombre).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=nombreconsulta, cantidad=cantidad)

    elif email != "":
        emailconsulta = Cliente.query.filter_by(emailCliente=email).all()

        if not email:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if email:
            cantidad = Cliente.query.filter_by(emailCliente=email).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=emailconsulta, cantidad=cantidad)

    elif direccion != "":
        direccionconsulta = Cliente.query.filter_by(
            direccionCliente=direccion).all()

        if not direccion:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if direccion:
            cantidad = Cliente.query.filter_by(
                direccionCliente=direccion).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=direccionconsulta, cantidad=cantidad)

    elif sucursal != "Sucursal del Cliente":
        sucursalconsulta = Cliente.query.filter_by(
            sucursalCliente=sucursal).all()

        if not sucursal:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if sucursal:
            cantidad = Cliente.query.filter_by(
                sucursalCliente=sucursal).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=sucursalconsulta, cantidad=cantidad)

    elif nivel != "":
        nivelconsulta = Cliente.query.filter_by(nivelCliente=nivel).all()

        if not nivel:
            flash('Cliente inexistente, ingrese otra busqueda')
            return redirect(url_for('conscliente.conscliente'))

        if nivel:
            cantidad = Cliente.query.filter_by(nivelCliente=nivel).count()
            flash('clientes existentes para la consulta realizada')
            return render_template('mostrarconsultaclientes.html',
                                   nombre=nivelconsulta, cantidad=cantidad)
