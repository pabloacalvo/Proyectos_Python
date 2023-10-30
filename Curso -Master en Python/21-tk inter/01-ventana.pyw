from tkinter import *
import os.path

class Programa:
    def __init__(self) :
        self.titulo = "Master en python"
        self.icon = './imagenes/icono.ico'
        self.icon_alt = './Curso -Master en Python/21-tk inter/imagenes/icono.ico'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        # Crear ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Cambiar tamaño
        ventana.geometry(self.size)

        # Titulo de la ventana
        ventana.title(self.titulo)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(ventana,text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Bloquear el tamaño de la vetana
        if  self.resizable == True:
            ventana.resizable(1,1) #Cambiar de 0 a 1 para Horizontal/Vertical
        else:
            ventana.resizable(0,0)
        
    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()
    
    # Arrancar y mostrar la ventana hasta que se cierre
    def mostrar(self):
        self.ventana.mainloop()

# Instanciar mi programa

programa = Programa()
programa.cargar()
programa.addTexto("Hola pablo crackkkk")
programa.mostrar()