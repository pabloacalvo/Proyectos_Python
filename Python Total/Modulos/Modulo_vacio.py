import Modulo_ocupado
from Mi_paquete import suma_y_resta
import unittest

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'Buen dia'
        resultado = Modulo_ocupado.todo_mayusculas(palabra)
        self.assertEquals(resultado, 'Buen Dia')



if __name__ == '__main___':
    unittest.main()