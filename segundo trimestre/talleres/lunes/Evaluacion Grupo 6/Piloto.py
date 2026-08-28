from MiembroEspacial import MiembroEspacial
class Piloto(MiembroEspacial):
    '''
    Clase que representa a un Piloto que hace parte de la agencia espacial.

    Attributes:
        horas_de_vuelo (int): indica las horas que lleva el piloto volando.
    '''
    horas_de_vuelo : int
    def __init__(self, nombre : str, edad : int, rango : str, horas_de_vuelo : int):
        '''
        Crea una nueva instancia del Piloto.
        
        Args:
            nombre (str): Nombre del piloto.
            edad (int): Edad del piloto.
            rango (str): Posicion del piloto.
            horas_de_vuelo: Cantidad de horas de vuelo
        '''
        super().__init__(nombre, edad, rango)
        self.horas_de_vuelo = horas_de_vuelo

    def pilotar_nave(self) -> str:
        '''
        Indicia que el piloto tomo ell control de los sistemas de navegacion.
    
        Returns:
            str: Mensaje indicando que el piloto tomo los sistemas de navegacion.
        '''
        return f'{self.nombre} a tomado el control de los sistemas de navegacion.'
    
    def registrar_entrenamiento(self, horas : int) -> None:
        '''
        Se analizan las horasd de entrenamiento

        Args:
            horas (int): horas realizadas por el piloto a agregar.
        '''
        horas_de_vuelo += horas
    
    def es_apto_para_mision(self):
        '''
        Analiza si el piloto puede ir a la mision.

        Returns:
            str: Mensaje de True si tiene mas de 500h de vuelo y False si no tiene
        '''
        horas_necesarias = 500
        if self.horas_de_vuelo > horas_necesarias:
            return True
        else:
            return False
