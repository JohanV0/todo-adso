from typing import List
from MiembroEspacial import MiembroEspacial
from Cohete import Cohete
from Piloto import Piloto
from Cientifico import Cientifico


class Mision:
    '''
    Representa una mision espacial que articula un cohete y una
    tripulacion bajo un nombre clave.

    Attributes:
        nombre_clave (str): Nombre clave de la mision.
        destino (str): Destino de la mision.
        cohete (Cohete): Cohete asignado a la mision.
        tripulantes (List[MiembroEspacial]): Lista de tripulantes asignados.
    '''

    def __init__(self, nombre_clave: str, destino: str, cohete: Cohete):
        '''
        Crea una nueva instancia de Mision.

        Args:
            nombre_clave (str): Nombre clave de la mision.
            destino (str): Destino de la mision.
            cohete (Cohete): Cohete ya creado que se asigna a la mision.
        '''
        self.nombre_clave = nombre_clave
        self.destino = destino
        self.cohete = cohete
        self.tripulantes = []

    def agregar_miembro(self, tripulante: MiembroEspacial) -> None:
        '''
        Agrega un tripulante a la lista de la mision. Acepta tanto objetos Piloto como Cientifico.

        Args:
            tripulante (MiembroEspacial): Tripulante a agregar a la mision.
        '''
        self.tripulantes.append(tripulante)

    def lista_miembro(self) -> str:
        '''
        Genera un listado en texto de todos los tripulantes de la mision.

        Returns:
            str: Texto con la lista numerada de tripulantes.
        '''
        tripulante_str = ""
        posicion = 0
        for miembro in self.tripulantes:
            posicion += 1
            tripulante_str += f"{posicion}. {miembro.presentarse()}\n"
        return tripulante_str

    def simulador(self) -> bool:
        '''
        Ejecuta la simulacion completa de despegue: valida que exista
        cohete y tripulantes, que haya al menos un piloto apto, y que
        la aceleracion estimada del cohete sea suficiente. Si todo es
        valido, activa el flujo de despegue.

        Returns:
            bool: True si el despegue es exitoso, False si se aborta
                  en cualquiera de las validaciones.
        '''
        if self.cohete is None or len(self.tripulantes) == 0:
            print("Error: la mision no cuenta con cohete asignado o no tiene tripulantes.")
            return False

        apto_mision = False
        for miembro in self.tripulantes:
            if type(miembro) == Piloto and miembro.es_apto_para_mision():
                apto_mision = True

        if not apto_mision:
            print("Error: no se encontro ningun piloto apto en la tripulacion.")
            return False

        aceleracion = self.cohete.calcular_aceleracion_estimada()
        if aceleracion < 1.5:
            print("Alerta: el cohete es demasiado pesado para despegar.")
            return False

        print(self.cohete.motor.encender_propulsor())
        for miembro in self.tripulantes:
            if type(miembro) == Piloto:
                print(miembro.pilotar_nave())
            elif type(miembro) == Cientifico:
                print(miembro.analizar_muestras())

        return True