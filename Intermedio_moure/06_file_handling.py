### Manejo de ficheros ###

import os

#.txt File

"""""txt_file = open("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.txt", "r+") #Leer y escribir
#print(txt_file.read()) #Leer
#print(txt_file.read(10)) #Leer 10 posiciones
print(txt_file.readline()) #Leer linea a linea
print(txt_file.readlines()) #Leer linea a linea y las devuelve en una lista cada linea es un elemento
txt_file.write("\nAunque tambien me gusta Javascript")
"""""



txt_file = open("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.txt", "w+") #Leer y escribir
#txt_file.write("Mi nombre es Pablo \n Mi apellido es Calvo \n Tengo 31 anos \n Y mi lenguaje preferido es Python")
#print(txt_file.read()) #Leer
#print(txt_file.read(10)) #Leer 10 posiciones
print(txt_file.readline()) #Leer linea a linea
print(txt_file.readlines()) #Leer linea a linea y las devuelve en una lista cada linea es un elemento""""""

txt_file.write("\nAunque tambien me gusta Javascript")
txt_file.close()

with open("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.txt", 'a') as my_other_file:
    my_other_file.write("\n Y Java")

#os.remove("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.txt")

# .json File

import json

json.dump  #Escribir el fichero

json_file = open("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.json", "w+")

json_text = {"name":"Pablo",
             "surname":"Calvo",
             "age":31,
             "languages":["Python","Java","Kotlin"],
             "website":"https//:google.com"}

json.dump(json_text, json_file,indent=2)
json_file.close()

with open("C:\\Users\pc250282\PycharmProjects\pythonProject\Intermedio\my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)