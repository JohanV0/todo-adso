# #funciones en python 

# '''
# Una funcion de un bloque de codigo que hace tarea especifica y al que se puede llamar cuando se necesite, sin repetir codigo. Sirve para organizar, reutilizar y simplificar programas

# def nombre(parametro1,paramero2,...):
#     #cuerpo de la funcion
# '''

# def saludar():
#     print('Hola, Bienvenido al curso de python')

# saludar()

# def saludar_persona(nombre):
#     print(f"Hola, {nombre}, ¿Como estás?")

# #saludar_persona(nombre=input('Digite su nombre: '))
# saludar_persona('Claudia')


# def sumar(a, b, c = 0):
#     suma = a + b + c
#     return suma

# sumar(4,5)
# resultado = sumar(4,5)
# print(f'Resultado: {resultado}')

# import random
# def lanzar_dado(caras):
#     return random.randint(1,caras)

# print(lanzar_dado(20))

# def restar(a,b):
#     resta = a - b
#     return resta

# print(f'Resta: {restar(b = 6, a = 4)}')

#########################################
# Argumentos de longitud variable
#########################################

def sumar(numeros):
    total = 0
    for i in numeros:
        total += i
    return total
print(sumar([1,2,3,4,5]))

def suma(*numeros):
    print(type(numeros))
    total = 0
    for n in numeros:
        total += n
    return total
print(suma(1,3,5,4))

def suma_dic (**kwargs):
    '''
    Descripcion de la funcion. Como debe ser usada, que parametros acepta y que devuelve:
    Calcula la suma de los valores de entrada. Recibe como entrada un diccionario con los datos a sumar ovarios parametros numericos. Retorna un numero con el resultado de los valores ingresados 
    '''
    suma = 0
    for key, value in kwargs.items():
        print(key,value)
        suma += value
    return(suma)
print(suma_dic.__doc__)
print(suma_dic(a=5,b=20,c=23,d=8))

def sumar_nuev(num1,num2,*nums):
    total = num1 + num2
    for n in nums:
        total += n
    return total

print(sumar_nuev(5,9,5,3,14))