#se guardan las listas 
nombres = ["Ana", "Luis", "María", "Carlos", "Sofía", "Pedro", "Laura", "Juan", "Valentina", "Diego"]
notas = [4.5, 3.8, 4.9, 2.7, 2.2, 4.1, 3.2, 4.7, 2.9, 3.6]

diccionario_notas = {k:v for k,v in zip(nombres,notas)}# k = clave -> con zip es nombres, v = valor -> con zip es notas 
print('-'*90)
print(diccionario_notas)#se imprime el diccionario 
print('-'*90)
#diccionarios donde se va a guardar cada una de las notas segun su clasficacion
notas_mayores = {}
notas_intermedias = {}
notas_bajas = {}

for j,c in diccionario_notas.items():# para j(clave) y c(valor) en diccionario_notas: 
    if c > 4.0:#si el valor es mayor a 4.0:
        notas_mayores[j] = c #se guarda en el diccionario de notas mayores la clave que tiene j con el valor igual al que lleva c
    elif c >= 3.0 and c <= 3.9:
        notas_intermedias[j] = c
    elif c <= 2.9 and c >= 2.7:
            c = round(c + 0.3 , 2)#como valentina aparece con 3.1999999999999999, esto hace que si queda ahi lo redondee a 3.2
            notas_intermedias[j] = c
    else:
        notas_bajas[j] = c

print(f"Notas altas: {notas_mayores}")
print(f"Notas intermedias: {notas_intermedias}")
print(f"Notas bajas: {notas_bajas}")