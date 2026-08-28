print('***Calculadora en python***')

SALIR = False

while not SALIR:
        print('''
    Operaciones que puedes realizar:
        1.Suma
        2.Resta
        3.Multiplicacion
        4.Division
        5.Salir
    ''')
        opcion = int(input('Escoge una opcion:'))
        if opcion == 1:
            valor_1 = int(input(f'Dame el valor del primer numero: '))
            valor_2 = int(input(f'Dame el valor del segundo numero: '))
            suma = valor_1 + valor_2
            print(f'El resultado de la suma es: {suma:.2f}')
        elif opcion == 2:
            valor_1 = int(input(f'Dame el valor del primer numero: '))
            valor_2 = int(input(f'Dame el valor del segundo numero: '))
            resta = valor_1 - valor_2
            print(f'El resultado de la resta es: {resta:.2f}')
        elif opcion == 3:
            valor_1 = int(input(f'Dame el valor del primer numero: '))
            valor_2 = int(input(f'Dame el valor del segundo numero: '))
            multiplicacion = valor_1 * valor_2
            print(f'El resultado de la suma es: {multiplicacion:.2f}')
        elif opcion == 4:
            valor_1 = int(input(f'Dame el valor del primer numero: '))
            valor_2 = int(input(f'Dame el valor del segundo numero: '))
            division = valor_1 / valor_2
            print(f'El resultado de la suma es: {division:.2f}')
        elif opcion == 5:
            SALIR = True
            print('Saliendo de la calucladora. ¡Hasta pronto!')
        else:
             print('Error ingrese un valor valido')
else:
     print('Estas fuera de la calculadora de python')