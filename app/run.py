from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from .auth import auth as auth_blueprint
#from .contacto import contacto2 as contacto_blueprint
from .ingresoproducto import insgresoproducto2 as insproducto_blueprint
from .consultaproducto import consproducto2 as consproducto_blueprint
from .mostrarconsulta import mosconsulta2 as mosconsulta_blueprint
from .mostrarconsulta import productostodos2 as productostodos_blueprint
from .ingresocliente import ingresocliente2 as inscliente_blueprint
from .consultaclientes import conscliente2 as conscliente_blueprint
from .consultaclientes import clientestodos2 as clientestodos_blueprint
from .consultaventas import consultaventas2 as consultaventas_blueprint
from .consultaventas import ventastodos2 as ventastodos_blueprint
from .consultapedidos import consultapedidos2 as consultapedidos_blueprint
from .consultapedidos import pedidostodos2 as pedidostodos_blueprint
from .mostrarpedidos import mospedidos2 as mospedidos_blueprint
from .mostrarpedidos import ventafinalizada2 as ventafinalizada_blueprint
from .bdd.models import User
from .bdd.models import db


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'clave'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://URI'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


app = create_app()

app.register_blueprint(auth_blueprint)
#app.register_blueprint(contacto_blueprint)
app.register_blueprint(consproducto_blueprint)
app.register_blueprint(mosconsulta_blueprint)
app.register_blueprint(insproducto_blueprint)
app.register_blueprint(inscliente_blueprint)
app.register_blueprint(conscliente_blueprint)
app.register_blueprint(clientestodos_blueprint)
app.register_blueprint(productostodos_blueprint)
app.register_blueprint(consultaventas_blueprint)
app.register_blueprint(ventastodos_blueprint)
app.register_blueprint(consultapedidos_blueprint)
app.register_blueprint(pedidostodos_blueprint)
app.register_blueprint(mospedidos_blueprint)
app.register_blueprint(ventafinalizada_blueprint)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', nombre=current_user.nombreUser)


@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')


if __name__ == '__main__':
    app.run(debug=True)
