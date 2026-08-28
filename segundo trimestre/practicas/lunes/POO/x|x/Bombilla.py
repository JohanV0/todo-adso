from Dispositivo_Inteligente import DispositivoInteligente

class Bombillo(DispositivoInteligente): 
    '''
    Clase que representa a un bombillo que hace parte de la clase dispositivo inteligente

    Attributes:
        nivel_brillo (float): Numero de la intesidad del brillo que tenga el bombillo
    '''

    nivel_brillo : str
    
    def __init__(self,nombre:str, porcentaje_bateria: str, nivel_brillo : str):
        '''
        Crea una nueva instancia de bombillo. 
        
        Args:
            nombre (str): Nombre del dispositivo.
            porcentaje_bateria (str): Numero del nivel de la bateria del dispositivo inteligente.
            nivel_brillo (float): Cantidad de brillo que ejecuta
        '''
        super().__init__(nombre,porcentaje_bateria) 
        self.nivel_brillo = nivel_brillo

    def ajustar_brillo(self) -> None:
        '''
        Se modifica ell nivel del brillo
        '''
        print(f'El dispositivo :{self.nombre} ahora tiene un nivel de brillo de: {self.nivel_brillo}')