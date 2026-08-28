class Empleado:
    nombre : str
    cedula : str 
    salario_base : float
    
    def __init__(self, nombre : str, cedula : str, salario_base : float):
        self.nombre = nombre
        self.cedula = cedula
        self.salario_base = salario_base
    def calcular_salario_neto(self) -> float:
        descuento = self.salario_base * 0.1
        return self.salario_base - descuento