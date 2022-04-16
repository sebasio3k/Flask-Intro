from flask import Flask, request, render_template, url_for, redirect, jsonify, session
from werkzeug.exceptions import abort

app = Flask(__name__)  # objeto de flask

app.secret_key = 'Mi_llave_secreta'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Omitimos validacion de usuario y password

        usuario = request.form['username']  # nombre igual a name de template
        # Agregar el usuario a la sesion:
        session['username'] = usuario
        # session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


# http://localhost:5000/
@app.route("/")
def inicio():
    if 'username' in session:
        return f'El usuario {session["username"]} ya ha hecho login'
    return 'No ha hecho login'

    # app.logger.debug('Mensaje a nivel debug')
    # app.logger.info(f'Entramos al path: {request.path}')
    # app.logger.warn('Mensaje a nivel warn')
    # app.logger.error('Mensaje a nivel ERROR')

    # return "<p>Hello, World! from flask</p>"


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu Edad es: {edad + 1}'


# GET: obtener informacion del servidor (listar)
# POST: enviar info al servidor
@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es {nombre}'


@app.route('/mostrar2/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre2(nombre):
    return render_template('mostrar.html', nombre_llave=nombre)


# Redireccionar a inicio:
@app.route('/redireccionar')
def redirecion():
    return redirect(url_for('inicio'))


@app.route('/redireccionar-mostrar2')
def redirecionar_mostrar2():
    return redirect(url_for('mostrar_nombre2', nombre='Juan'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


# REST Representational State Transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)
    # return {'nombre': nombre}
