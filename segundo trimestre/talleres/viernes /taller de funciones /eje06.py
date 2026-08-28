def calcular_estadisticas(ventas_diarias):
    contenedor_suma = 0
    for n in ventas_diarias:
        sumar = n + n
        contenedor_suma += sumar / 2
    maximo = sorted(ventas_diarias)
    minimo = sorted(ventas_diarias, reverse=True)
    return contenedor_suma, maximo, minimo

def calcular_promedio(ventas_diarias):
    mayor = ventas_diarias[0]
    posicion = 0
    contenedor_suma = 0
    for n in ventas_diarias:
        sumar = n + n
        contenedor_suma += sumar / 2
    prom = contenedor_suma / len(ventas_diarias)
    for n in range(len(ventas_diarias)):
        if ventas_diarias[n] > mayor:
            mayor = ventas_diarias[n]
            posicion = n
            if posicion == 0:
                posicion = 'Lunes'
            elif posicion == 1:
                posicion = 'Martes'
            elif posicion == 2:
                posicion = 'Miercoles'
            elif posicion == 3:
                posicion = 'Jueves'
            elif posicion == 4:
                posicion = 'Viernes'
            elif posicion == 5:
                posicion = 'Sabado'
            else:
                posicion = 'Domingo'
    return posicion, prom

lista_ventas = [
    float(input('Digite la venta del lunes: ')), 
    float(input('Digite la venta del martes: ')), 
    float(input('Digite la venta del miercoles: ')),
    float(input('Digite la venta del jueves: ')),
    float(input('Digite la venta del viernes: ')), 
    float(input('Digite la venta del sabado: ')),
    float(input('Digite la venta del domingo: '))]

suma, maximo, minimo =  calcular_estadisticas(lista_ventas)
posicion,promedio = calcular_promedio(lista_ventas)
print(f'''
Valor máximo : {maximo[0]:.1f}
Valor mínimo : {minimo[0]:.1f}
Suma de los valores: {suma}
El dia con mayor venta es: {posicion}
El promedio de ventas es de: {promedio:.2f}
''')