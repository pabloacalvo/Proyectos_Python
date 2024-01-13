from flask import Flask, render_template, jsonify,request
import requests
from clases.error import Error
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(405)
def method_not_allowed(error):
    ex=Error(error)
    return jsonify(ex.getError())

@app.errorhandler(404)
def method_not_allowed(error):
    ex=Error(error)
    return jsonify(ex.getError())

@app.errorhandler(500)
def method_not_allowed(error):
    ex=Error(error)
    return jsonify(ex.getError())

@app.route('/crear_socio',methods=["POST"])
def crearSocio():
    """Metodo de creacion de socio"""
    socioJson=json.loads(request.data)
    return "hola"

@app.route('/pagos')
def verPagos():
    url = 'https://localhost:7100/Pagos/Reporte'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        # response_json= response.json() #obtenemos un diccionario
        jsonPagos = response.json()
    return jsonPagos

@app.route('/datos-socios')
def verSocios():
    url = 'https://localhost:7100/socios/allSocios'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        jsonSocios = response.json()
    return jsonSocios

@app.route('/test')
def get_json():
    response = requests.get('https://localhost:7100/socios/allSocios',verify=False)
    data = response.json()
    # Genera el contenido HTML de la tabla
    table_content = '<table>'

    # Crea la cabecera de la tabla con las claves del primer elemento del JSON
    table_content += '<tr>'
    for key in data[0].keys():
        table_content += f'<th>{key}</th>'
    table_content += '</tr>'

    # Itera sobre los elementos del JSON y genera las filas de la tabla
    for item in data:
        table_content += '<tr>'
        for value in item.values():
            table_content += f'<td>{value}</td>'
        table_content += '</tr>'

    # Cierra la tabla
    table_content += '</table>'
    return render_template('table.html', data=table_content)

#valido archivo que arranca la aplicacion
if __name__ == '__main__':
    app.run(debug=True)