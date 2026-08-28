class MiembroEspacial:
    '''
    Representa a un miembro inscrito en la agencia espacial.

    Attributes:
        nombre (str): El nombre completo del miembro de la agencia espacial.
        edad (int): La edad actual del miembro de la agencia espacial.
        rango (str): Puesto que ocupa el miembro en la agencia espacial.
    '''
    nombre : str
    edad : int
    rango : str

    def __init__(self, nombre : str, edad : int, rango : str):
        """
        Inicializa un miembro de la agencia espacial.
        
        Args:
            nombre (str): Nombre del miembro,
            edad (int): Edad actual
            rango (str): Rango actual del miembto.
        """
        self.nombre = nombre
        self.edad = edad
        self.rango = rango
    def presentarse (self) -> str:
        """
        Indicia una presentacion del miembto actual con su informacion 

        Returns: 
            str: devuelve la informacion del usuario con el nombre, edad y rango
        """
        return f"Nombre: {self.nombre}, Rango: {self.rango}, Edad: {self.edad}"
    
