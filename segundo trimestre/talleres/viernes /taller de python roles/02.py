numero_secreto = 3
intento1 = int(input(f'Ingrese un numero en el rango de 1 a 5: '))

intento2 = int(input(f'Ingrese un numero en el rango de 1 a 5: '))

if intento1 == numero_secreto and intento2 == numero_secreto:
    abs = (intento1+intento2) - numero_secreto
    distancia = 0
    print(f'''
    Has leído la mente del oráculo.
    intentos: 2 
    distancia: {distancia} numeros
''')
    if intento1 > intento2:
        print(f'el numero {intento1} estuvo mas cerca del numero secreto')
    elif intento1 < intento2:
        print(f'el numero {intento2} estuvo mas cerca del numero secreto')
    elif intento1 == intento2:
        print(f'Ambos numero quedaron a la misma distancia del numero secreto')

elif intento1 == 2 or intento1 == 4 and intento2 == 2 or intento2 == 4:
    abs = (intento1+intento2) - numero_secreto
    if intento1 > numero_secreto:
        distancia_numero_1 = intento1 - numero_secreto
    elif intento1 < numero_secreto:
        distancia_numero_1 = numero_secreto - intento1
    if intento2 > numero_secreto:
        distancia_numero_2 = intento2 - numero_secreto
    elif intento1 < numero_secreto:
        distancia_numero_2 = numero_secreto - intento2
    print(f'''
    Muy cerca... el oráculo siente tu energía.
    intentos: 2
    distancia del numero uno al numero secreto: {distancia_numero_1} numeros
    distancia del numero dos al numero secreto: {distancia_numero_2} numeros
''')
    if intento1 > intento2:
        print(f'el numero {intento1} estuvo mas cerca del numero secreto')
    elif intento1 < intento2:
        print(f'el numero {intento2} estuvo mas cerca del numero secreto')
    elif intento1 == intento2:
        print(f'Ambos numero quedaron a la misma distancia del numero secreto')

elif intento1 == 1 or intento1 == 5 and intento2 == 1 or intento2 == 5:
    print(f'Lejos aun. El oraculo rie en las sombras.')
    abs = (intento1+intento2) - numero_secreto
    if intento1 > numero_secreto:
        distancia_numero_1 = intento1 - numero_secreto
    elif intento1 < numero_secreto:
        distancia_numero_1 = numero_secreto - intento1
    if intento2 > numero_secreto:
        distancia_numero_2 = intento2 - numero_secreto
    elif intento1 < numero_secreto:
        distancia_numero_2 = numero_secreto - intento2
    print(f'''
    Muy cerca... el oráculo siente tu energía.
    intentos: 2
    distancia del numero uno al numero secreto: {distancia_numero_1} numeros
    distancia del numero dos al numero secreto: {distancia_numero_2} numeros
''')
    if intento1 > intento2:
        print(f'el numero {intento1} estuvo mas cerca del numero secreto')
    elif intento1 < intento2:
        print(f'el numero {intento2} estuvo mas cerca del numero secreto')
    elif intento1 == intento2:
        print(f'Ambos numero quedaron a la misma distancia del numero secreto')
    
elif intento1 < 0 or intento1 > 5:
    print(f'Solo puedes elegir entre 1 y 5')
else:
    print(f'Eso no es un número. El oraculo te ignora.')
