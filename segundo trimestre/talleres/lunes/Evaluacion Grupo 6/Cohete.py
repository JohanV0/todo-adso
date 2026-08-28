from Motor import Motor

class Cohete:
    '''
    Representa el cohete que sera utilizado en la mision con su motor.

    Attributes:
        nombre (str): Nombre del cohete.
        peso_toneladas (float): Peso del cohete en toneladas.
        motor (Motor): Motor incorporado al cohete (composicion).
    '''
    def __init__(self, nombre: str, peso_toneladas: float, modelo_motor: str, empuje_kn: float):
        '''
        Crea una nueva instancia de Cohete, instanciando su propio Motor.

        Args:
            nombre (str): Nombre del cohete.
            peso_toneladas (float): Peso del cohete en toneladas.
            modelo_motor (str): Modelo del motor a instanciar.
            empuje_kn (float): Empuje del motor a instanciar, en kilonewtons.
        '''
        self.nombre = nombre
        self.peso_toneladas = peso_toneladas
        self.motor = Motor(modelo_motor, empuje_kn) 
        
    def calcular_aceleracion_estimada(self) -> float:
        '''
        Calcula la aceleracion estimada del cohete, en funcion del
        empuje de su motor y su peso total.

        Returns:
            float: Aceleracion estimada del cohete, en m/s^2.
        '''
        aceleracion = self.motor.empuje_kn / self.peso_toneladas
        return aceleracion