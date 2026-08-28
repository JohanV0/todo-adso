class Mascota:
    '''
    
    '''
    nombre : str
    especie : str

    def __init__(self, nombre : str, especie : str):
        self.nombre = nombre
        self.especie = especie
    
    def presentarse(self):
        print(f"{self.nombre} -> ({self.especie})")
        