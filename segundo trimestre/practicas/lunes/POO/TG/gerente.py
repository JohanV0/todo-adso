class Gerente:
    #------------
    #Atributos
    #-----------
    nombre: str
    documento : str

    #-------------
    # constructor
    #-------------

    def __init__(self,nombre : str, documento : str ):
        self.nombre = nombre 
        self.documento = documento
    
    #--------------
    # Metodos 
    #--------------


    def obtener_perfil(self) -> str:
        '''Devuelve una cadena con los datos del gerente.'''
        return f"{self.nombre} (CC {self.documento})"
    