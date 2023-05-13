from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import current_user
from .bdd.models import Cliente, Pedido, User, Venta, db
import arrow

mospedidos2 = Blueprint('mospedidos', __name__)
ventafinalizada2 = Blueprint('ventafinalizada', __name__)


@mospedidos2.route('/mospedidos')
def mospedidos():
    idPedido = request.args.get('idPedido')
    idCliente = request.args.get('idCliente')
    idUsuario = request.args.get('idUsuario')
    idProducto = request.args.get('idProducto')
    estadoPedido = request.args.get('estadoPedido')

    if (idPedido == "" and idCliente == "" and idUsuario == ""
            and idProducto == "" and estadoPedido == "Estado del Pedido"):
        flash('Por favor, complete algún parámetro para la busqueda')
        return redirect(url_for('conspedidos.conspedidos'))

    elif idPedido != "":
        consulta = Pedido.query.filter_by(idPedido=idPedido).first()

        if not consulta:
            flash('Pedido inexistente, ingrese otra busqueda')
            return redirect(url_for('conspedidos.conspedidos'))

        if consulta:
            flash('pedidos existentes para la consulta realizada')
            return render_template('mostrarconsultapedidos.html',
                                   nombre=consulta, cantidad=1)
    elif idCliente != "":
        consulta = Pedido.query.filter_by(idClientePedido=idCliente).all()

        if not consulta:
            flash('Pedido inexistente, ingrese otra busqueda')
            return redirect(url_for('conspedidos.conspedidos'))

        if consulta:
            cantidad = Pedido.query.filter_by(
                idClientePedido=idCliente).count()
            flash('pedidos existentes para la consulta realizada')
            return render_template('mostrarconsultapedidos.html',
                                   nombre=consulta, cantidad=cantidad)

    elif idUsuario != "":
        consulta = Pedido.query.filter_by(idUsuarioPedido=idUsuario).all()

        if not consulta:
            flash('Pedido inexistente, ingrese otra busqueda')
            return redirect(url_for('conspedidos.conspedidos'))

        if consulta:
            cantidad = Pedido.query.filter_by(
                idUsuarioPedido=idUsuario).count()
            flash('pedidos existentes para la consulta realizada')
            return render_template('mostrarconsultapedidos.html',
                                   nombre=consulta, cantidad=cantidad)

    elif idProducto != "":
        consulta = Pedido.query.filter_by(idProductoPedido=idProducto).all()

        if not consulta:
            flash('Pedido inexistente, ingrese otra busqueda')
            return redirect(url_for('conspedidos.conspedidos'))

        if consulta:
            cantidad = Pedido.query.filter_by(
                idProductoPedido=idUsuario).count()
            flash('pedidos existentes para la consulta realizada')
            return render_template('mostrarconsultapedidos.html',
                                   nombre=consulta, cantidad=cantidad)

    elif estadoPedido != "Estado del Pedido":
        consulta = Pedido.query.filter_by(estadoPedido=estadoPedido).all()

        if not consulta:
            flash('Pedido inexistente, ingrese otra busqueda')
            return redirect(url_for('conspedidos.conspedidos'))

        if consulta:
            cantidad = Pedido.query.filter_by(
                estadoPedido=estadoPedido).count()
            flash('pedidos existentes para la consulta realizada')
            return render_template('mostrarconsultapedidos.html',
                                   nombre=consulta, cantidad=cantidad)


@mospedidos2.route('/mospedidos', methods=['POST', 'GET'])
def mospedidos_post():
    cliente = current_user.dniUser #request.form.get('cliente')

    if cliente == "":
        flash('Para finalizar la venta tiene que ingresar el Codigo de Cliente')
        return redirect(url_for('mospedidos.mospedidos'))

    if cliente != "":
        consultacliente = User.query.filter_by(dniUser=cliente).first()

        if not consultacliente:
            flash('No existe el Cliente en la base de datos')
            return redirect(url_for('mospedidos.mospedidos'))

        if consultacliente:
            idUsuarioVenta = current_user.id
            diaVenta = arrow.now().format('YYYY-MM-DD HH:mm:ss')
            estadoVenta = "Pendiente"
            #sucursalVenta = current_user.sucursalUser

            consulta = Pedido.query.filter_by(
                idClientePedido=cliente, estadoPedido="Pendiente").first()

            if not consulta:
                flash('Los pedidos ya fueron Procesados')
                return redirect(url_for('mospedidos.mospedidos'))

            if consulta:
                consulta = Pedido.query.filter_by(
                    idClientePedido=cliente, estadoPedido="Pendiente").all()
                total = 0
                for consulta in consulta:
                    total = float(consulta.valorPedido) + total

                #nivelcliente = int(consultacliente.nivelCliente)

                #if nivelcliente == 1:
                #    total = total - total * 0.2

                #if nivelcliente == 2:
                #    total = total - total * 0.15

                #if nivelcliente == 3:
                #    total = total - total * 0.1

                #if nivelcliente == 4:
                #    total = total - total * 0.05

                #if nivelcliente == 5:
                #    total = total

                ventaagregar = Venta(idClienteVenta=cliente,
                                     idUsuarioVenta=idUsuarioVenta,
                                     diaVenta=diaVenta,
                                     estadoVenta=estadoVenta,
                                     #sucursalVenta=sucursalVenta,
                                     valorVenta=total)

                db.session.add(ventaagregar)
                db.session.commit()

                pedidos = Pedido.query.filter_by(idClientePedido=cliente).all()
                consulta2 = Venta.query.filter_by(
                    idClienteVenta=cliente).first()

                for pedidos in pedidos:
                    pedidos.idVentaPedido = int(consulta2.idVenta)
                    pedidos.estadoPedido = "Procesado"
                    db.session.commit()

                consulta = Venta.query.filter_by(idClienteVenta=cliente).all()
                cantidad = Venta.query.filter_by(
                    idClienteVenta=cliente).count()

                consulta = Venta.query.filter_by(idClienteVenta=cliente).all()
                cantidad = Venta.query.filter_by(
                    idClienteVenta=cliente).count()

                flash('ventas.')
                return render_template('ventafinalizada.html',
                                       nombre=consulta, cantidad=cantidad)


@ventafinalizada2.route('/ventafinalizada')
def ventafinalizada():
    return render_template('ventafinalizada.html')


@ventafinalizada2.route('/ventafinalizada', methods=['POST', 'GET'])
def ventafinalizada_post():
    venta = request.form.get('venta')
    if venta:
        consulta = Venta.query.filter_by(idVenta=venta).all()
        for consulta in consulta:
            consulta.estadoVenta = "Procesada"
            db.session.commit()

        consulta = Venta.query.filter_by(idVenta=venta).all()
        cantidad = Venta.query.filter_by(
            idVenta=venta).count()
        flash('ventas finalizadas')
        return render_template('mostrarconsultaventas.html',
                               nombre=consulta, cantidad=cantidad)
