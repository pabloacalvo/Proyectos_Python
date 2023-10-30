"""
Crear uun programa que tenga:
-Ventana
-Tamanio fijo
-No defimensinoable
-Un menu(Inicio, Añadir, Informacion(), Salir)
-Diferentes pantallas
-Formulario de anadir productos
-Guardar datos temporalmente
-Mostrar datos listados en la pantalla principal
-Opcion de salir
"""

from tkinter import *
from tkinter import ttk
#Crear ventana
ventana =Tk()
#ventana.geometry('400x400')
ventana.minsize(500,500)
ventana.title('Proyecto TkInter Master en Python')
ventana.resizable(0,0)

#Pantallas

def home():
    #Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()
    home_label.config(fg='white',bg='black',font=('Arial',30),padx=63,pady=20)
    home_label.grid(row=0,column=0)
    products_box.grid(row=2)
    
    #Listar productos
    """
    for product in products:
        if len(product) == 3:
            #Con esto len se convierte en 4 y con la proxima iteracion no se muestra duplicado
            product.append('added')
            Label(products_box,text=product[0]).grid()
            Label(products_box,text=product[1]).grid()
            Label(products_box,text=product[2]).grid()
            Label(products_box,text='---------------').grid()
    """
    for product in products:
        if len(product) == 3:
            product.append('added')
            products_box.insert('',0,text=product[0],values=(product[1]))

def add():
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    add_label.config(fg='white',bg='black',font=('Arial',30),padx=60,pady=20)
    add_label.grid(row=0,column=0,columnspan=10)

    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    add_price_label.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    add_price_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
    add_description_label.grid(row=3,column=0,sticky=NW)
    add_description_entry.grid(row=3, column=1,sticky=W)
    add_description_entry.config(width=30,height=5,font=('Consolas',12),padx=15,pady=15)
    add_separator.grid(row=4,column=1)
    boton.grid(row=5,column=1,sticky=NW)
    boton.config(padx=15,pady=5,bg='green',fg='white')
    


def info():
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    info_label.config(fg='white',bg='black',font=('Arial',30),padx=100,pady=20)
    info_label.grid(row=0,column=0)
    data_label.grid(row=1,column=0)


def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get('1.0','end-1c')
    ])
    name_data.set('')
    price_data.set('')
    add_description_entry.delete('1.0','end-1c')
    home()



#Definir campos de pantalla
home_label = Label(ventana,text='Pagina de inicio')
#products_box = Frame(ventana,width=250)
Label(ventana).grid(row=1)

products_box = ttk.Treeview(height=12,columns=2)
products_box.grid(row=1, column=0,columnspan=2)
products_box.heading('#0',text='Producto',anchor=W)
products_box.heading('#1',text='Precio',anchor=W)

add_label = Label(ventana,text='Añadir productos')
info_label= Label(ventana,text='Información')
data_label = Label(ventana,text='Creado por Pablo Calvo - 2023')

#Variables
products = []
name_data = StringVar()
price_data = StringVar()



#Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame,text='Nombre:')
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame,text='Precio:')
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame,text='Descripción:')
add_description_entry = Text(add_frame)
add_separator = Label(add_frame)

boton = Button(add_frame,text='Guardar',command=add_product)

#Ocultar pantallas
home_label.grid_remove()
add_label.grid_remove()
info_label.grid_remove()
data_label.grid_remove()
home


#Cargar pantalla de inicio
home()

#Crear menu
mi_menu = Menu(ventana)
mi_menu.add_command(label='Inicio',command=home)
mi_menu.add_command(label='Añadir',command=add)
mi_menu.add_command(label='Información',command=info)
mi_menu.add_command(label='Salir', command=ventana.quit)


# Cargar menu
ventana.config(menu=mi_menu)















ventana.mainloop()