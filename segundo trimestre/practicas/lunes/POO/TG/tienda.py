from gerente import Gerente
class Tienda:
    #--------
    # Atributos
    #--------

    nombre : str 
    direccion : str 
    gerente : Gerente

    #--------------
    # Constructor 
    #--------------
    
    def __init__(self, nombre : str, direccion : str):
        self.nombre = nombre
        self.direccion = direccion
        self.gerente = None

    #--------------
    # Gerente
    #--------------

    def asignar_gerente(self, gerente : Gerente) -> None:
        self.gerente = gerente
    
    def mostrar_ficha(self) -> None:
        print(f'--- Ficha del establecimiento: {self.nombre}')
        print(f'Ubicacion: {self.direccion}')
        if self.gerente is None:
            print("Puesto de Gerente vacante")
        else:
            print(f"Gerente: {self.gerente.obtener_perfil()}")