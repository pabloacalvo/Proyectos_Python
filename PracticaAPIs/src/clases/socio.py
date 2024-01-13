##Clase modelo socio
class socio():

    def __init__(self,socio):
        if(socio):
            self.IdSocio = socio['IdSocio']
            self.nombre = socio['nombre']
            self.apellido = socio['apellido']
            self.dni = socio['dni']
            self.telefono = socio['telefono']
            self.nombreGenero = socio['nombreGenero']
            self.fechDeInscripcion = socio['fechaDeInscripcion']
            self.nombreEstado = socio['nombreEstado']
            self.fechaUltimoPago = socio['fechaUltimoPago']
            self.nombreAbono = socio['nombreAbono']
            self.fk_IdAbonoSocio = socio['fk_IdAbonoSocio']
