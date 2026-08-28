class Viaje:
    '''
    Clase que representa un viaje realizado por un conductor a un cliente 
    '''

    origen : str
    destino : str
    distancia : int 
    costo : float
    def __init__(self,origen : str, destino : str, distancia : str, costo : float):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.costo = costo
        