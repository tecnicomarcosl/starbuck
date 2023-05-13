from flask import render_template, redirect, url_for, request, flash, Blueprint


consproducto2 = Blueprint('consproducto', __name__)


@consproducto2.route('/consproducto')
def consproducto():
    return render_template('consultaproducto.html')


@consproducto2.route('/consproducto', methods=['POST', 'GET'])
def consproducto_post():
    nombre = request.form.get('nombre')
    codigo = request.form.get('codigo')
    rubro = request.form.get('rubro')
    marca = request.form.get('marca')

    if codigo == "" and nombre == "" and marca == "" and rubro == "Rubro":
        flash('Por favor, complete algún parámetro para la busqueda')
        return redirect(url_for('consproducto.consproducto'))

    else:

        return redirect(url_for('mosconsulta.mosconsulta', nombre=nombre,
                                codigo=codigo, rubro=rubro, marca=marca))
