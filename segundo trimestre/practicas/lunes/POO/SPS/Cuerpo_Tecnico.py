from Miembro_Seleccion import MiembroSeleccion

class CuerpoTecnico(MiembroSeleccion):
    '''
    Representa a un miembro del cuerpo tecnico de la seleccion.

    attributes:
        rol (str): Rol del integrante del cuerpo tecnico.
        expereiencia_anios (int): Numero de años de expereiencia.
    '''

    rol : str
    experiencia_anios : int

    def __init__(self, nombre : str, pasaporte: str, rol : str, experiencia_anios : int):
        '''
        Inicializa in nievo miembro del equipo tenico de la seleccion.

        Args:
            nombre (str): Nombre del integrante cuerpo tecnico.
            pasaporte (str): Numero de pasaporte del integrante del cuerpo tecnico.
            rol (str): Rol dentro del cuerpo tecnico.
            experiencia_anios (int): Cantidad de años de experiencia.
        '''
        super().__init__(nombre, pasaporte)
        self.rol = rol
        self.experiencia_anios = experiencia_anios

    def dar_instrucciones(self) -> None:
        '''
        Representa las intrucciones que se dan dentro y fuera de la cancha.
        '''
        print(f'{self.nombre}, en su rol de {self.rol}, ordena cambios tacticos desde el banco.')
