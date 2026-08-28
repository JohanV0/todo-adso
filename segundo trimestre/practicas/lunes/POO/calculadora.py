
def sumar (a,b,c = 0):
    
    return a + b + c

def restar (a,b,c = 0):

    return a - b - c

def multiplicar (a, b):
    
    return a * b

def dividir (a,b):
    
    return a / b

def programa_principal():
    print('-' * 30)
    print('Bienvenido a la calculadora')
    print('-' * 30)
    
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese otro numero entero: "))

    print('-' * 30)
    salir = False
    while not salir:
        print('Seleccione su operacion a relizar: ')
        print('1.Suma')
        print('2.Resta')
        print('3.multiplicacion')
        print('4.division')
        print('5.salir')
        opcion = int(input())
        print('-' * 30)

        while opcion < 1 or opcion > 4:
            opcion = int(input("Ingrese una opcion valida: "))
        match opcion:
            case 1:
                resultado = sumar(num1, num2)
            case 2:
                resultado = restar(num1, num2)
            case 3:
                resultado = multiplicar(num1, num2)
            case 4:
                resultado = dividir(num1, num2)
            case 5:
                print('Saliendo del sistema... Adios')
                break
        print(f'El resultado de la operacion es: {resultado}')
        print('-' * 30)
        print()

programa_principal()
