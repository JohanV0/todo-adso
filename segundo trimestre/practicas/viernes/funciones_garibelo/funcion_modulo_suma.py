print("**Funciones en Python**")

#declaramos una funcion de suma
def sumar(a, b):
    resultado_suma= a + b
    return resultado_suma

resultado_suma = sumar(2,4)
print(f'Resultado funcion sumar: {resultado_suma}')

#volvemos a llamar la funcion 

resultado_suma= sumar(9,15)
print(f'Resultado funcion sumar: {resultado_suma}')



#funcion llamada persona creando parametros "nombre "apellido", "edad"
def persona(nombre, apellido, edad):
    print(f'Su nombre es {nombre} {apellido} y tiene {edad} años ')

persona("Juan", "Hernandez", "21")