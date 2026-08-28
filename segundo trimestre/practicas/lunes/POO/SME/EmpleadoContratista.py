from Empleado import Empleado
class EmpleadoContratista(Empleado):
    def calcular_salario_neto(self) -> float:
        estampilla = self.salario_base * 0.02
        return self.salario_base - estampilla
    