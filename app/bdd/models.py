from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    dniUser = db.Column(db.Integer, unique=True)
    emailUser = db.Column(db.String(50), unique=True)
    passwordUser = db.Column(db.String(100))
    nombreUser = db.Column(db.String(50))
#    tipoUser = db.Column(db.String(15))
#    sucursalUser = db.Column(db.String(20))


#class Contacto(db.Model):
#    __tablename__ = "contacto"
#    id = db.Column(db.Integer, primary_key=True)
#    emailContacto = db.Column(db.String(25), unique=True)
#    nombreContacto = db.Column(db.String(50))
#    consultaContacto = db.Column(db.String(2000))


class Cliente(db.Model):
    __tablename__ = "cliente"
    idCliente = db.Column(db.Integer, primary_key=True)
    dniCliente = db.Column(db.Integer, unique=True)
    nombreCliente = db.Column(db.String(50))
    emailCliente = db.Column(db.String(50), unique=True)
    direccionCliente = db.Column(db.String(100))
    sucursalCliente = db.Column(db.String(20))
    nivelCliente = db.Column(db.Integer)


class Producto(db.Model):
    __tablename__ = "producto"
    idProducto = db.Column(db.Integer, primary_key=True)
    valorProducto = db.Column(db.Float)
    marcaProducto = db.Column(db.String(100))
    nombreProducto = db.Column(db.String(50))
    rubroProducto = db.Column(db.String(50))
    stockProducto = db.Column(db.Integer)
    sucursalProducto = db.Column(db.String(50))


class Venta(db.Model):
    __tablename__ = "venta"
    idVenta = db.Column(db.Integer, primary_key=True)
    idClienteVenta = db.Column(db.Integer)
    idUsuarioVenta = db.Column(db.Integer)
    diaVenta = db.Column(db.DateTime)
    estadoVenta = db.Column(db.String(15))
    sucursalVenta = db.Column(db.String(20))
    valorVenta = db.Column(db.Float)


class Pedido(db.Model):
    __tablename__ = "pedido"
    idPedido = db.Column(db.Integer, primary_key=True)
    idClientePedido = db.Column(db.Integer)
    idUsuarioPedido = db.Column(db.Integer)
    idProductoPedido = db.Column(db.String(50))
    cantidadProductoPedido = db.Column(db.Integer)
    valorPedido = db.Column(db.Float)
    estadoPedido = db.Column(db.String(15))
    idVentaPedido = db.Column(db.Integer)
