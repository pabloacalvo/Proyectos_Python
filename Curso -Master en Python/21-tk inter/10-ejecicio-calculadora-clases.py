from tkinter import *
from tkinter import messagebox as MessageBox

class Calculadora:

    def __init__(self,alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas
        

    def setFloat(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            self.alertas.showerror('Error','Introduce datos correctos')
        return result

    def sumar(self):
        
        self.resultado.set(self.setFloat(self.numero1.get()) + self.setFloat(self.numero2.get()))
        self.mostrar_resultado()
    
            
    def restar(self):
        self.resultado.set(self.setFloat(self.numero1.get()) - self.setFloat(self.numero2.get()))
        self.mostrar_resultado()

    def multiplicar(self):
        self.resultado.set(self.setFloat(self.numero1.get()) * self.setFloat(self.numero2.get()))
        self.mostrar_resultado()

    def dividir(self):
        if (self.setFloat(self.numero2.get())) == 0:
            self.alertas.showerror('Error','No se puede dividir entre cero')
        else:
            self.resultado.set(self.setFloat(self.numero1.get()) / self.setFloat(self.numero2.get()))
            self.mostrar_resultado()

    def mostrar_resultado(self):
        self.alertas.showinfo('Resultado',f'El resultado de la operacion es {self.resultado.get()}')
        self.numero1.set('')
        self.numero2.set('')

ventana = Tk()
ventana.title('Ejercicio completo con TkInter')
ventana.geometry('400x400')
ventana.config(
    bd=25)

calculadora = Calculadora(MessageBox)

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd = 5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
Label(marco, text='Primer numero: ').pack()
Entry(marco, textvariable=calculadora.numero1, justify='center').pack()
Label(marco, text='Segundo numero: ').pack()
Entry(marco, textvariable=calculadora.numero2,justify='center').pack()
Label(marco, text='').pack()
Button(marco, text='SUMAR', command=calculadora.sumar).pack(side='left', fill=X, expand=YES)
Button(marco, text='RESTAR', command=calculadora.restar).pack(side='left', fill=X, expand=YES)
Button(marco, text='MULTIPLICAR', command=calculadora.multiplicar).pack(side='left', fill=X, expand=YES)
Button(marco, text='DIVIDIR', command=calculadora.dividir).pack(side='left', fill=X, expand=YES)
ventana.mainloop()