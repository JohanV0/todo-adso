class Pasajero:
    '''
    Clase que implementa un pasajero/cliente empresarial
    '''
    nombre : str
    telefono : str
    nombre_empresa : str
    tiene_credito : bool
    
    def __init__(self,nombre : str, telefono : str, nombre_empresa : str, tiene_credito : bool):
        self.nombre = nombre
        self.movil = telefono
        self.nombre_empresa = nombre_empresa
        self.tiene_credito = tiene_credito
        