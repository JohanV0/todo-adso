vida = 100
monedas = 0 
print(f'\n bienvenido al juego de elegir tu destino')
bosque = input('¿Desea cruzar o rodear el rio?: (cruzar o redear)').lower().strip()
if bosque == 'cruzar':
    vida -= 40
    monedas =  50
    print(f'Usted decidio cruzar el bosque, tiene {vida}/100 de vida y {monedas} monedas')
    cueva = input(f'Encontro una cueva, desea ir a la izquierda o derecha: (derecha o izquierda)').lower().strip()

    if cueva == 'izquierda':
        prueba = int(input(f'Cuanto es 5 + 3 = ?: '))
        solucion = 8

        if prueba == solucion:
            monedas += 100
            vida == vida
            print(f'Correcto usted lleva {vida}/100 y lleva {monedas} monedas')
            torre = input(f'Encontro una torre desea subir o negociar: ')

            if torre == 'subir':
                monedas += 80
                vida += 30
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            elif torre == 'negociar':
                monedas += 40
                vida += 5
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            else:
                print(f'Error solo puede elegir subir o negociar')

        elif prueba != solucion:
            monedas-=10
            vida -= 40
            print(f'Incorecto usted lleva {vida}/100 y lleva {monedas} monedas')
            torre = input(f'Encontro una torre desea subir o negociar: (subir o negociar)').lower().strip()

            if torre == 'subir':
                monedas += 80
                vida += 30
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            elif torre == 'negociar':
                monedas += 40
                vida += 5
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            else:
                print(f'Error solo puede elegir subir o negociar')
        else:
            print('Error el valor ingresado debe ser numero')
    
    elif cueva == 'derecha':
        monedas += 0
        vida -= 50
        print(f'Usd decidio ir por la derecha y no gano monedas, su vida es de {vida}')
        torre = input(f'Encontro una torre desea subir o negociar: (subir o negociar)'.lower().strip())
        if torre == 'subir':
            monedas += 80
            vida += 30
            print(f'''
                Usted decidio subir.
                Felicidades por completar el juego.
                vida total: {vida}
                Monedas Totales: {monedas}''')
        elif torre == 'negociar':
            monedas += 40
            vida += 5
            print(f'''
                Usted decidio subir.
                Felicidades por completar el juego.
                vida total: {vida}
                Monedas Totales: {monedas}''')
    else:
        print(f'Error solo puede elegir ir por la derecha o izquierda')

elif bosque == 'rodear':
    vida -= 20
    monedas =  10
    print(f'Usted decidio cruzar el bosque, tiene {vida}/100 de vida y {monedas} monedas')
    cueva = input(f'Encontro una cueva, desea ir a la izquierda o derecha: (izquerda o derecha)').lower().strip()

    if cueva == 'izquierda':
        prueba = int(input(f'Cuanto es 5 + 3 = ?: '))
        solucion = 8

        if prueba == solucion:
            monedas += 100
            vida == vida
            print(f'Correcto usted lleva {vida}/100 y lleva {monedas} monedas')
            torre = input(f'Encontro una torre desea subir o negociar: ')

            if torre == 'subir':
                monedas += 80
                vida += 30
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            elif torre == 'negociar':
                monedas += 40
                vida += 5
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            else:
                print(f'Error solo puede elegir subir o negociar')

        elif prueba != solucion:
            monedas-=10
            vida -= 40
            print(f'Incorecto usted lleva {vida}/100 y lleva {monedas} monedas')
            torre = input(f'Encontro una torre desea subir o negociar: ')

            if torre == 'subir':
                monedas += 80
                vida += 30
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            elif torre == 'negociar':
                monedas += 40
                vida += 5
                print(f'''
                    Usted decidio subir.
                    Felicidades por completar el juego.
                    vida total: {vida}
                    Monedas Totales: {monedas}''')
            else:
                print(f'Error solo puede elegir subir o negociar')
        else:
            print('Error el valor ingresado debe ser numero')
    
    elif cueva == 'derecha':
        monedas += 0
        vida -= 50
        print(f'Usd decidio ir por la derecha y no gano monedas, su vida es de {vida}')
        torre = input(f'Encontro una torre desea subir o negociar: (subir o negociar)').lower().strip()
        if torre == 'subir':
            monedas += 80
            vida += 30
            print(f'''
                Usted decidio subir.
                Felicidades por completar el juego.
                vida total: {vida}
                Monedas Totales: {monedas}''')
        elif torre == 'negociar':
            monedas += 40
            vida += 5
            print(f'''
                Usted decidio subir.
                Felicidades por completar el juego.
                vida total: {vida}
                Monedas Totales: {monedas}''')
    else:
        print(f'Error solo puede elegir ir por la derecha o izquierda')
else:
    print('Ese camino no esta en su camino')