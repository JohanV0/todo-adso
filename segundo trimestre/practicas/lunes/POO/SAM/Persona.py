#cuando la relacion asociada unidireccional, la relacion se convierte un atributo de la que no tiene la flecha
from typing import List
from Mascota import Mascota

class Persona:
    nombre : str
    edad : int 
    mascotas : List[Mascota]

    def __init__(self, nombre : str, edad : int):
        self.nombre = nombre
        self.edad = edad
        self.mascotas = []

    def agregar_mascota(self, mascota : Mascota) -> str:
        self.mascotas.append(mascota)
        return f"{mascota.nombre} fue adoptada por {self.nombre}"
    
    def listar_mascotas(self) -> str:
        mascotas_str = ""
        posicion = 0
        for mascota in self.mascotas:
            posicion += 1
            mascotas_str += f"{posicion}. {mascota.nombre} ({mascota.especie})\n"
        
        return mascotas_str
    
# Persona -> conferencia 
# Mascota -> Asistente