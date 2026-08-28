class Motor:
    '''
    Representa el motor de propulsion incorporado en un cohete.

    Attributes:
        modelo (str): Modelo o denominacion tecnica del motor.
        empuje_kn (float): Potencia de empuje del motor, medida en kilonewtons.
    '''
    modelo : str
    empuje_kn : float
    def __init__(self, modelo : str, empuje_kn : float):
        self.modelo = modelo
        self.empuje_kn = empuje_kn
    def encender_propulsor(self) -> str:
        '''
        Enciende el propulsor del motor para iniciar la secuencia de despegue.

        Returns:
            str: Mensaje confirmando que el motor ha sido encendido.
        '''
        return f'El motor {self.modelo} ha sido encendido, generando {self.empuje_kn} kN de empuje.'
    