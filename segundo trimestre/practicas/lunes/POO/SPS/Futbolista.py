from Miembro_Seleccion import MiembroSeleccion
 
class Futbolista(MiembroSeleccion): #eN PARENETESIS SE INDICA DE DONDE HEREDA 
    '''
    Clase que representa a un futbolista que hace parte de la seleccion.

    Attributes:
        numero_camiseta (int): Numero que representa al numero de la camiseta del jugador de las seleccion.
        posicion (str): Posicion en la que juega el futbolista.
    '''

    numero_camiseta : str
    posicion: str
    
    def __init__(self,nombre:str, pasaporte: str, numero_camiseta : str, posicion : str):
        '''
        Crea una nueva instancia de Futbolista.
        
        Args:
            nombre (str): Nombre del futbolista.
            pasaporte (str): Numero de pasaporte del Futbolista
            numero_camiseta (int): Numero de la camiseta del fubolista.
            posicion (str): Posicion en la que uega el futbolista. 
        '''
        super().__init__(nombre,pasaporte) #Super para invocar los atributos de la clase padre .__init__ para el metodo constructor y los parametros que va a usar.
        self.numero_camiseta = numero_camiseta
        self.posicion = posicion

    def jugar_partido(self) -> None:
        '''
        Pone a jugar al fubtolista.
        '''
        print(f'{self.nombre}(N°{self.numero_camiseta}) salta a la cancha como {self.posicion}')