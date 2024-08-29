from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Aprediendo flask'

@app.route('/informacion')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre=None, apellidos=None):
    texto = ''
    if nombre != None and apellidos != None:
        texto = f'<h3>Bienvenido, {nombre} {apellidos}</h3>'

    return f"""
        <h1>Pagina de informacion</h1>
        <h3>Esta es la informacion</h3>
        <p>{texto}</p>
    """

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):
    if redireccion != None:
        return redirect(url_for('lenguajes'))
    else:
        return '<h1>Pagina de contacto</h1>'

@app.route('/lenguajes')
def lenguajes():
    return '<h1>Pagina de lenaguajes</h1>'

if __name__ == '__main__':
    app.run(debug=True)