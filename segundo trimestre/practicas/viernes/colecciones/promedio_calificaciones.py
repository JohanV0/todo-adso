#Promedio de calificaciones 

Notas = []
salir = False
notas_ingresadas = 0
while not salir:
    Nota = float(input('Digite su nota: '))
    notas_ingresadas += 1 
    Notas.append(Nota)
    suma_notas = Notas + Notas
    prom = suma_notas / notas_ingresadas
    salida = input('Si desea salir digite "s" si desea continuar presione enter: ')
    if salida == 's':
        salir = True
        print(f'Notas ingresadas: {notas_ingresadas}')