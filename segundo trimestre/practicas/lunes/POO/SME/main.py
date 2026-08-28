from Empleado import Empleado
from EmpleadoContratista import EmpleadoContratista
from EmpleadoDiretivo import EmpleadoDirectivo

empleado_regular = Empleado('ana lopez','4151368431',2_000_000.0)
empleado_contratista = EmpleadoContratista('Carlos Ruiz', '111131543',2_500_000)
empleado_directivo = EmpleadoDirectivo('Maria Gomez', '651654646',7_000_000,800_000)

if __name__ == '__main__':
    print(empleado_regular.calcular_salario_neto())
    print(empleado_contratista.calcular_salario_neto())
    print(empleado_directivo.calcular_salario_neto())
