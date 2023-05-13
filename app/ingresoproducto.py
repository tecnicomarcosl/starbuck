from flask import render_template, redirect, url_for, request, flash, Blueprint
from .bdd.models import Producto, db


insgresoproducto2 = Blueprint('insproducto', __name__)


@insgresoproducto2.route('/insproducto')
def insproducto():
    return render_template('ingresoproducto.html')


@insgresoproducto2.route('/insproducto', methods=['POST', 'GET'])
def insproducto_post():
    nombre = request.form.get('nombre')
    marca = request.form.get('marca')
    rubro = request.form.get('rubro')
    stock = request.form.get('stock')
    valor = request.form.get('valor')
    sucursal = request.form.get('sucursal')

    if (nombre == "" or marca == "" or rubro == "Rubro" or stock == ""
            or valor == "" or sucursal == "Sucursal"):
        flash('Por favor, complete correctamente todos los datos del producto')
        return redirect(url_for('insproducto.insproducto'))

    if (nombre != "" and marca != "" and rubro != ""
            and stock != "" and valor != ""):
        productoagregar = Producto.query.filter_by(
            nombreProducto=nombre, marcaProducto=marca, rubroProducto=rubro,
            valorProducto=valor, stockProducto=stock,
            sucursalProducto=sucursal).first()

        if not productoagregar:
            productoagregar = Producto(nombreProducto=nombre,
                                       marcaProducto=marca, rubroProducto=rubro,
                                       stockProducto=stock, valorProducto=valor,
                                       sucursalProducto=sucursal)

            db.session.add(productoagregar)
            db.session.commit()
            flash('Producto agregado')
            return redirect(url_for('insproducto.insproducto'))

        if productoagregar:
            flash('Producto existente')
            return redirect(url_for('insproducto.insproducto'))
