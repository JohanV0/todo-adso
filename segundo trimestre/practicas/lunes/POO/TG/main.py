from gerente import Gerente
from tienda import Tienda

def simular_franquicia():
    print('=== Sistema RetaiFlow ===')
    gerente1= Gerente(nombre='Luis Martinez',documento='1230987456')
    tienda_jordan = Tienda(nombre='Tienda Jordan',direccion='Et. 22 Mz 102 Cs 302')

    tienda_jordan.mostrar_ficha()

    tienda_jordan.asignar_gerente(gerente1)
    tienda_jordan.mostrar_ficha()




if __name__ == "__main__":
    simular_franquicia()