#variables necesarias
salir = False
acumuluador = 0
acumuluador_nota = 0
promedio = 0
notas_mayor_prom = 0
notas_menor_prom = 0

while not False:#mientras no sea verdadero siga
    nota = float( input('Ingrese la nota del estudiantes (0.0/5.0) y ingrese -1 para salir: '))# si la nota es float guardela en nota
    if nota >= 0.0 and nota <= 5.0:# ranfo de la nota , si cumple aumenta el acumulador de notas, se guarda la nota, se saca el prom si hay mas de una nota 
        acumuluador += 1
        acumuluador_nota += nota
        if acumuluador > 1:
            promedio = acumuluador_nota / acumuluador

        if nota > promedio:#Se guarda si la nota es mayor al prom
            notas_mayor_prom += 1
        elif nota < promedio:#Se guarda si la nota es menor al prom
            notas_menor_prom += 1
    elif nota > 5.0:#Se muestra si la nota es mayor al prom
        print('Nota ingresada no es valida')
    elif nota == -1:#Si se presiona -1 sale del programa y muestra el print
        salir == True
        print(f'''
Promedio: {promedio}
Notas encima del promedio: {notas_mayor_prom}
Notas debajo del promedio: {notas_menor_prom}
Saliendo...
''')
        break
    else:
        print('Nota ingresada NO es un NUMERO')#Si no es float no cuenta y se repite el mensaje de la variable nota
else:
    print('Salio del promedio de calificaciones de un grupo')