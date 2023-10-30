import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nOk, vamos a registrarnos")
        nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa el contraseña: ")
        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"El registro de {registro[1].nombre} fue exitoso \nDatos de ingreso: \nEmail: {registro[1].email}")
        else:
            print("Hubo un error en el registro")

    def login(self):
        print("Identicate en el sistema")
        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa el contraseña: ")
            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"Bienvenido {login[1]}, tu fecha de registro fue el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e).__name__)   
            print("Login incorrecto")

    def proximasAcciones(self, usuario):
        print("""
        -Crear nota (crear)
        -Mostrar notas (mostrar)
        -Eliminar nota (eliminar)
        -Salir
        """)
        hazEl = notas.acciones.Acciones()
        accion = input("Elegi la opcion deseada: ")
        if accion.lower() =='crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == 'mostrar':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == 'eliminar':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion.lower() == 'salir':
            print(f"Has salido {usuario[1]}")
            exit()