import request
import json

import requests

#request simple

url = 'https://rickandmortyapi.com/api/character/64'
request = requests.get(url)
json_response = request.json()
print(json_response)
status = json_response['status']
print(status)
indice = 1
while indice < 11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(indice)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status =j['status']
    print(f'El personaje {name} su estado es :{status}')
    indice += 1

#request episodio 1

url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
personajes = j['characters']
list_names = []
list_human = []
list_others = []
for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    list_names.append(name)
    if js['species'] == 'Human':
        list_human.append(name)
    else:
        list_others.append(name)


print(list_human)
print(list_others)