class DispositivoInteligente:
    '''
    Representa a un elemento inteligente registrado.
    
    Atributos:
        nombre (str): El nombre completo del dispositivo inteligente.
        porcentaje_bateria (str): Numero del nivel de la bateria del dispositivo inteligente.
    '''
        
    nombre : str 
    porcentaje_bateria = str 

    def __init__(self,nombre : str, porcentaje_bateria = str):
        self.nombre = nombre
        self.porcentaje_bateria = porcentaje_bateria

    def conexion_internet(self,conexion_red : str) -> None:
        """
        Indica si el usuario esta conectado a la red domestica
        
        Args:
            conexion_red(str): verifica si el usuario esta conectado a la red domestica.
        """
        print(f'El dispositivo :{self.nombre} esta conectado a la red: {conexion_red}')