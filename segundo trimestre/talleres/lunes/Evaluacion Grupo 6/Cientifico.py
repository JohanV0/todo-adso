from MiembroEspacial import MiembroEspacial
class Cientifico(MiembroEspacial):
    '''
    Clase que representa a un cientifico que hace parte de la agencia espacial.

    Attributes:
        area_investigacion (str): lugar donde el cientifico actualmente esta trabajando.
    '''
    area_investigacion : str
    def __init__(self, nombre : str, edad : int, rango : str, area_investigacion : str):
        '''
        Crea una nueva instancia de Cientifico.
        
        Args:
            nombre (str): Nombre del cientifico.
            edad (int): Edad del cientifico.
            rango (str): Posicion del cientifico.
            area_investigacion (str): lugar donde trabaja el cientifico
        '''
        super().__init__(nombre, edad, rango)
        self.area_investigacion = area_investigacion
    def analizar_muestras(self) -> str:
        '''
        Analiza las muestras recolectadas por el cientifico.

        Returns:
            str: Mensaje indicando el resultado del analisis.
        '''
        return f"El cientifico: {self.nombre} esta en el area: {self.area_investigacion} evaluando unas muestras."
