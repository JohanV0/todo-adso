#se crea la clase con la palabra reservada 
class Empleado:
    '''
    Esta clase reperesenta a un empleado de la empresa
    '''

# metodo constructor se encarga de construir objetos
# para el metodo contructor los parametros son los atributos de la clase 
    
    def __init__(self, nombre: str, cedula: int, direccion: str, salario_base:float, porcentaje_retencion:float):
        self.nombre:str = nombre
        self.__cedula:int = cedula
        self.direccion:str = direccion
        self.salario_base: float = salario_base
        self.porcentaje_retencion: float = porcentaje_retencion

    def get_cedula(self) -> int:
        '''
        Retorna el valor de la cedula del empleado
        '''
        return self.__cedula
    
    def set_cedula(self, nueva_cedula) -> None:
        '''
        Permite modificar la cedula del empleado SOLO si cumple con las condiciones
        '''
        if nueva_cedula >= 1_000 and nueva_cedula <= 1_999_999_999:
            self.cedula = nueva_cedula
            print(f'Se asigno la nueva cedula {nueva_cedula} satisfactoriamente')
        else:
            print(f'No se puede asignar la cedula {nueva_cedula} por que no es valido ')


    def get_salario_base(self) -> float:
        '''
        Retorna el valor del salario base del empleado
        '''
        return self.__salario_base
    
    def set_salario_base(self, nueva_salario_base) -> None:
        '''
        Permite modificar el salario base del empleado SOLO si cumple con las condiciones
        '''
        if nueva_salario_base >= 0:
            self.__salario_base = nueva_salario_base
            print(f'Se asigno el nuevo salario base {nueva_salario_base} satisfactoriamente')
        else:
            print(f'No se puede asignar el salario base {self.salario_base} por que no es valido ')


empleado1 = Empleado("Carlos Mendoza", 11102345, "Calle 6 Avenida 3", 3000, 12.0)

print(f'Empleado: {empleado1.get_cedula()}')