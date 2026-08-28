class MiembroSeleccion:
    '''
    Representa a un miembro de la seleccion para realizar la gestion de los viajes al mundial.
    
    Atributos:
        nombre (str): El nombre completo del miembro de la selccion.
        pasaporte (str): Numero de pasaporte del miembro de la selección.
    '''

    nombre:str
    pasaporte:str

    def __init__(self,nombre:str,pasaporte:str):
        """
        Inicializa un miembro de la seleccion.
        
        Args:
            nombre (str): Nombre del miembro,
            pasaporte (str): Pasaporte del miembro.
        """
        self.nombre = nombre
        self.pasaporte = pasaporte

    def viajar(self, destino:str) -> None:
        """
        Indica el viaje a realizar por el miembro de la seleccion.
        
        Args:
            destino(str): Destino al cual viaja el miembro.
        """
        print(f"{self.nombre} viaja con la seleccion hacia {destino} para los octavos de final.")