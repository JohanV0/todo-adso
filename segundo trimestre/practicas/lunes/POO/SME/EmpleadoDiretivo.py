from Empleado import Empleado

class EmpleadoDirectivo(Empleado):
    bono_ejecutivo = float

    def __init__(self, nombre: str, cedula : str, salario_base : float, bono_ejecutivo : float):
        super().__init__(nombre, cedula, salario_base)
        self.bono_ejecutivo = bono_ejecutivo

    def calcular_salario_neto(self):
        salario_total = self.salario_base + self.bono_ejecutivo
        return salario_total * 0.9
    