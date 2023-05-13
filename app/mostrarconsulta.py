from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import current_user
from .bdd.models import Producto, Cliente, Pedido, User, db

mosconsulta2 = Blueprint('mosconsulta', __name__)
productostodos2 = Blueprint('productostodos', __name__)


@productostodos2.route('/productostodos')
def productostodos():
    nombreconsulta = Producto.query.all()
    cantidad = Producto.query.count()
    flash('productos existentes para la consulta realizada')
    return render_template('mostrarconsulta.html',
                           nombre=nombreconsulta, cantidad=cantidad)


@mosconsulta2.route('/mosconsulta')
def mosconsulta():
    #codigo = request.args.get('codigo')
    nombre = request.args.get('nombre')
    rubro = request.args.get('rubro')
    marca = request.args.get('marca')

    #if codigo != "":
    #    codigoconsulta = Producto.query.filter_by(idProducto=codigo).all()
    #    cantidad = Producto.query.filter_by(idProducto=codigo).count()

    #    if not codigoconsulta:
    #        flash('Producto inexistente, ingrese otra busqueda')
    #        return redirect(url_for('consproducto.consproducto'))

    #    if codigoconsulta:
    #        flash('productos existentes para la consulta realizada')
    #        return render_template('mostrarconsulta.html',
    #                               nombre=codigoconsulta, cantidad=cantidad)

    if nombre != "":
        nombreconsulta = Producto.query.filter_by(nombreProducto=nombre).all()

        if not nombreconsulta:
            flash('Producto inexistente, ingrese otra busqueda')
            return redirect(url_for('consproducto.consproducto'))

        if nombreconsulta:
            cantidad = Producto.query.filter_by(nombreProducto=nombre).count()
            flash('productos existentes para la consulta realizada')
            return render_template('mostrarconsulta.html',
                                   nombre=nombreconsulta, cantidad=cantidad)

    elif rubro != "Rubro":
        rubroconsulta = Producto.query.filter_by(rubroProducto=rubro).all()

        if not rubro:
            flash('Producto inexistente, ingrese otra busqueda')
            return redirect(url_for('consproducto.consproducto'))

        if rubro:
            cantidad = Producto.query.filter_by(rubroProducto=rubro).count()
            flash('productos existentes para la consulta realizada')
            return render_template('mostrarconsulta.html',
                                   nombre=rubroconsulta, cantidad=cantidad)

    elif marca != "":
        marcaconsulta = Producto.query.filter_by(marcaProducto=marca).all()

        if not marcaconsulta:
            flash('Producto inexistente, ingrese otra busqueda')
            return redirect(url_for('consproducto.consproducto'))

        if marcaconsulta:
            cantidad = Producto.query.filter_by(marcaProducto=marca).count()
            flash('productos existentes para la consulta realizada')
            return render_template('mostrarconsulta.html',
                                   nombre=marcaconsulta, cantidad=cantidad)


@mosconsulta2.route('/mosconsulta', methods=['POST', 'GET'])
def mosconsulta_post():
    cantidad = int(request.form.get('cantidad'))
    cliente = current_user.dniUser #request.form.get('cliente')
    codigo = request.form.get('codigo')

    if cliente == "" or cantidad == "" or codigo == "":
        flash('Para agregar el producto a un pedido tiene que ingresar Cantidad y Numero de Cliente')
        return redirect(url_for('consproducto.consproducto'))

    elif cliente != "" and cantidad != "" and codigo != "":
        clientepedido = User.query.filter_by(dniUser=cliente).first()

        if not clientepedido:
            flash('No existe el Cliente en la base de datos')
            return redirect(url_for('consproducto.consproducto'))

        if clientepedido:
            consulta = Producto.query.filter_by(idProducto=codigo).first()

            if not consulta:
                flash('Codigo de producto inexistente')
                return redirect(url_for('consproducto.consproducto'))

            if consulta:
                consultacantidad = int(consulta.stockProducto)
                if consultacantidad < cantidad:
                    flash('No hay esa cantidad de stock del producto seleccionado')
                    return redirect(url_for('consproducto.consproducto'))

                if consulta and consultacantidad >= cantidad:
                    pedidoeagregar = Pedido(idUsuarioPedido=current_user.id,
                                            idClientePedido=cliente,
                                            idProductoPedido=consulta.nombreProducto,
                                            cantidadProductoPedido=cantidad,
                                            valorPedido=int(
                                                consulta.valorProducto)*cantidad,
                                            estadoPedido="Pendiente",
                                            idVentaPedido=0)

                    db.session.add(pedidoeagregar)
                    stockactual = consultacantidad-cantidad
                    consulta.stockProducto = stockactual
                    db.session.commit()

                    flash('Pedido agregado')
                    return redirect(url_for('consproducto.consproducto'))
