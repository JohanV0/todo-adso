#Variables necesarias 
requisito = 16 and 30
conteo_edad = 0
contendor = 0
while True:#Mienras no sea verdadero siga:
    edad = int(input('Digite su edad para la inscripcion: (-1 para salir): '))#Se pide y guarda la edad ingresada por el usuario 
    if edad >=16 and edad <= 30:#Si esta en el rango de 16 a 30 se aumenta el conteo de edad,se guarda el valor de la edad y se saca el prom
        conteo_edad += 1
        contendor += edad
        if conteo_edad > 1:
            prom = contendor / conteo_edad
    else:
        print('Su edad no cumple con el requisito (entre 16 y 30)')#SI no esta en el rango se muestra el mensaje 
    if edad == -1:#Si se escribe -1 se sale del programa y muestra el total de aprobados y promedio por edad
        print(f'''
saliendo.....
total aprobados {conteo_edad}
promedio de edad: {prom}''')