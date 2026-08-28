class Conductor:
    '''
    Clase que representa a un conductor con su vehiculo 
    '''
    nombre : str
    licencia : str
    calificacion : float
    modelo_vehiculo : str
    placa : str
    esta_disponible: bool 

    def __init__(self, nombre : str, licencia : str, calificacion : float, modelo_vehiculo : str, placa : str):
        self.nombre = nombre
        self.licencia = licencia
        self.calificacion = calificacion
        self.modelo_vehiculo = modelo_vehiculo
        self.placa = placa
        self.esta_disponible = True
        