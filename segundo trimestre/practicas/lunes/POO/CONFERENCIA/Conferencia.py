from typing import List
from Asistente import Asistente
class Conferencia:
    titulo = str 
    hora = str 
    asistentes = List[Asistente]

    def __init__(self, titulo : str, hora : str):
        self.titulo = titulo
        self.hora = hora
        self.asistentes = []

    def registro_de_asistente(self, asistente : Asistente) -> str:
        self.asistentes.append(asistente)
        print('='*130)
        if asistente.nombre == "" and asistente.correo=="":
            return "No hay asistentes para agregar \n" 
        else:
            return f"El/La asistente {asistente.nombre} fue agregado \n" 
    
    def lista_asistente(self) -> str:
        asistente_str = ""
        posicion = 0
        print(f'*** Lista actualmente de la conferencia: {self.titulo} ***')
    
        if self.asistentes == []:
            return (f'- No hay asistentes actualmente agregados en la conferencia \n')
        else:
            for asistente in self.asistentes:
                posicion += 1
                asistente_str += f"{- posicion}. {asistente.nombre}\n"
            return asistente_str
    