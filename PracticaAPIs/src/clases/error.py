class Error():
    def __init__(self,error):
        self.error = error

    def getError(self):
        """METODO RETORNO DE ERRORES"""
        return [
            {'response':None,
             'error':str(self.error)
             }
        ]