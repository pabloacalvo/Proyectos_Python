import requests
import json
if __name__ == '__main__':
    url='https://localhost:7100/socios/allSocios'
    response = requests.get(url, verify=False)
    if response.status_code==200:
        #response_json= response.json() #obtenemos un diccionario
        json=response.json()
        print(json)
    for socio in json:
        name=socio['nombre']
        print(name)

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
    return table_content

