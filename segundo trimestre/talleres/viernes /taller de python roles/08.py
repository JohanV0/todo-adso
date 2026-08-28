acuerdo = input('desea participar en el juego? (si/no)')== 'si', 'no'

if acuerdo == 'si':
    print('Pruebas superadas: (0/2)')
    print('prueba 1:')
    acertijo_1 = input('Responda el acertijo: Tengo ciudades, pero no casas, montañas, pero no árboles, agua, pero no peces. ¿Que soy?: "').lower().strip() == 'mapa'
    if acertijo_1 == 'mapa':
        print('Bien hecho, ahora la prueba 2: ')
        print('Pruebas superadas: 1/2')
        acertijo_2 = input(f'Elige el simbolo (sol/luna/estrella): ').lower().strip()=='sol','luna','estrella'
        if acertijo_2 == 'sol':
            print("El sol no guarda este secreto." )
        elif acertijo_2 == 'luna':
            print('Pruebas superadas (2/2)')
            print("Has abierto el portal sagrado!")
            acertijo_oculto = input('felicidades encontraste el acertijo oculto, el ultimo es: Cuantas lunas tiene la Tierra?: ')
            if acertijo_oculto == 'tierra':
                print('felicidades de verdad abriste el portal oculto')
            else:
                print('lo siento no pudiste con el ultimo acertijo')
        elif acertijo_2 == 'estrella':
            print("Las estrellas guían pero no abren." )
        else:
            print("Eso no es un símbolo del ritual." )
    else:
        print("Fallaste la primera prueba.")
elif acuerdo == 'no':
    print('de acuerdo, no vas a participar en el juego')