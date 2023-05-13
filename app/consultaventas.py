from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Venta


consultaventas2 = Blueprint('consventa', __name__)
ventastodos2 = Blueprint('ventastodos', __name__)


@ventastodos2.route('/ventastodos')
def ventastodos():
    consulta = Venta.query.all()
    if not consulta:
        flash('No hay Ventas')
        return redirect(url_for('consventa.consventa'))

    if consulta:
        cantidad = Venta.query.count()
        flash('compras existentes para la consulta realizada')
        return render_template('ventafinalizada.html',
                               nombre=consulta, cantidad=cantidad)


@consultaventas2.route('/consventa')
def consventa():
    return render_template('consultaventa.html')


@consultaventas2.route('/consventa', methods=['POST', 'GET'])
def consventa_post():
    idVenta = request.form.get('idVenta')
    idCliente = request.form.get('idCliente')
    idUsuario = request.form.get('idUsuario')
    estadoVenta = request.form.get('estadoVenta')
    sucursalVenta = request.form.get('sucursal')

    if (idVenta == "" and idCliente == "" and idUsuario == ""
            and estadoVenta == "Estado de la Venta"
            and sucursalVenta == "Consultar por Sucursal"):
        flash('Por favor, complete algún parámetro para la busqueda')
        return redirect(url_for('consventa.consventa'))

    elif idVenta != "":
        consulta = Venta.query.filter_by(idVenta=idVenta).all()

        if not consulta:
            flash('Venta inexistente, ingrese otra busqueda')
            return redirect(url_for('consventa.consventa'))

        if consulta:
            flash('ventas existentes para la consulta realizada')
            return render_template('ventafinalizada.html',
                                   nombre=consulta, cantidad=1)
    elif idCliente != "":
        consulta = Venta.query.filter_by(idClienteVenta=idCliente).all()

        if not consulta:
            flash('Venta inexistente, ingrese otra busqueda')
            return redirect(url_for('consventa.consventa'))

        if consulta:
            cantidad = Venta.query.filter_by(idClienteVenta=idCliente).count()
            flash('ventas existentes para la consulta realizada')
            return render_template('ventafinalizada.html',
                                   nombre=consulta, cantidad=cantidad)

    elif idUsuario != "":
        consulta = Venta.query.filter_by(idUsuarioVenta=idUsuario).all()

        if not consulta:
            flash('Venta inexistente, ingrese otra busqueda')
            return redirect(url_for('consventa.consventa'))

        if consulta:
            cantidad = Venta.query.filter_by(idUsuarioVenta=idUsuario).count()
            flash('ventas existentes para la consulta realizada')
            return render_template('ventafinalizada.html',
                                   nombre=consulta, cantidad=cantidad)
    elif estadoVenta != "":
        consulta = Venta.query.filter_by(estadoVenta=estadoVenta).all()

        if not consulta:
            flash('Venta inexistente, ingrese otra busqueda')
            return redirect(url_for('consventa.consventa'))

        if consulta:
            cantidad = Venta.query.filter_by(estadoVenta=estadoVenta).count()
            flash('ventas existentes para la consulta realizada')
            return render_template('ventafinalizada.html',
                                   nombre=consulta, cantidad=cantidad)

    elif sucursalVenta != "":
        consulta = Venta.query.filter_by(sucursalVenta=sucursalVenta).all()

        if not consulta:
            flash('Venta inexistente, ingrese otra busqueda')
            return redirect(url_for('consventa.consventa'))

        if consulta:
            cantidad = Venta.query.filter_by(
                sucursalVenta=sucursalVenta).count()
            flash('ventas existentes para la consulta realizada')
            return render_template('ventafinalizada.html',
                                   nombre=consulta, cantidad=cantidad)
