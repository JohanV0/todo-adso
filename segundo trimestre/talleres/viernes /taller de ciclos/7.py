#variables necesarias
salir = False
contenedor_ventas = 0
intentos = 0
suma = 0
while not salir:#mientras no sea verdadero siga
    valor_venta = float(input('ingrese el valor de la venta en positivo: '))#Se guarda el valor de la venta
    if valor_venta == float(valor_venta):#Si el valor de la venta es float aumente el contador de intetos y guarde la venta 
        intentos += 1
        contenedor_ventas += valor_venta
        salida = input('Ingrese 0 para salir, 1 para continuar: ')#Si quierre salir o continuar
        if salida == '0':#Si se presiono 0 se hace la suma y se muestran los datos sacados
            suma = contenedor_ventas / intentos
            salir = True
            print(f'''
Total acumulado: {contenedor_ventas:.2f}
Promedio de ventas por transaccio: {suma:.2f}''')
        elif salida == '1':#Si se presiono 1 repita 
            continue
    else:
        print('El valor ingresado no es un numero')#Se muestra ell mensaje y se muestra de nuevo el input de valor_venta
else:
    print('Salida del Acumulador de ventas')