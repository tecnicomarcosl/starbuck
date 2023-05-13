from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Pedido


consultapedidos2 = Blueprint('conspedidos', __name__)
pedidostodos2 = Blueprint('pedidostodos', __name__)


@pedidostodos2.route('/pedidostodos')
def pedidostodos():
    consulta = Pedido.query.filter_by(estadoPedido="Pendiente").all() #Pedido.query.all()
    if not consulta:
        flash('No hay Pedidos por procesar. Busque un producto y arme el suyo')
        return redirect(url_for('consproducto.consproducto'))
        #return redirect(url_for('conspedidos.conspedidos'))

    if consulta:
        cantidad = Pedido.query.filter_by(estadoPedido="Pendiente").count()
        flash('pedidos pendientes')
        return render_template('mostrarconsultapedidos.html',
                               nombre=consulta, cantidad=cantidad)


@consultapedidos2 .route('/conspedidos')
def conspedidos():
    return render_template('consultapedidos.html')


@consultapedidos2.route('/conspedidos', methods=['POST', 'GET'])
def conspedidos_post():
    idPedido = request.form.get('idPedido')
    idCliente = request.form.get('idCliente')
    idUsuario = request.form.get('idUsuario')
    idProducto = request.form.get('idProducto')
    estadoPedido = request.form.get('estadoPedido')

    if (idCliente == ""):
        flash('Por favor, complete algún parámetro para la busqueda')
        return redirect(url_for('conspedidos.conspedidos'))

    else:

        return redirect(url_for('mospedidos.mospedidos', idPedido=idPedido,
                                idCliente=idCliente, idUsuario=idUsuario,
                                idProducto=idProducto, estadoPedido=estadoPedido))
