print(f'\nBienvenido al juego de Corte del Reino: Veredicto del Rey \n\nJugador 1:')
JUGADOR_1 = input('digite su rol (rey / sirviente / invasor) y hay un rol oculto: ').lower().strip()

print(f'''\nJugador 2:''')
JUGADOR_2 = input('digite su rol (rey / sirviente / invasor)y hay un rol oculto: ').lower().strip()

if JUGADOR_1 == 'aliado' or JUGADOR_2 == 'aliado':
    print(f'Tregua diplomatica declarada')
elif JUGADOR_1 == JUGADOR_2:
    print(f'\nEmpate. La corte queda en equilibrio.\nSe solicita el poder politico\n\nJugador 1:')
    poder_politico_jugador_1 = int(input('Porfavor Jugador 1 digite su poder politico (1 a 10):'))
    print(f'Jugador 2:')
    poder_politico_jugador_2 = int(input('Porfavor Jugador 2 digite su poder politico (1 a 10): ')) 
    if poder_politico_jugador_1 > poder_politico_jugador_2:
        print(f'el jugador 1 gana por mayor poder politico')
    elif poder_politico_jugador_1 == poder_politico_jugador_2:
        print(f'Empate absoluto')
    else:
        print(f'el jugador 2 gana por mayor poder politico')

elif JUGADOR_1 == 'rey' and JUGADOR_2 == 'sirviente' or JUGADOR_1 == 'sirviente' and JUGADOR_2 == 'rey':
    
    if JUGADOR_1 == 'rey':
        print(f'el jugador jugador 1 gana por elegir {JUGADOR_1}')
    elif JUGADOR_1 == 'sirviente':
        print(f'el jugador 2 gana por elegir {JUGADOR_2}')
    else:
        print(f'error')
elif JUGADOR_1 == 'sirviente' and JUGADOR_2 == 'invasor' or JUGADOR_1 == 'invasor' and JUGADOR_2 == 'sirviente':
    
    if JUGADOR_1 == 'sirviente':
        print(f'el jugador jugador 1 gana por elegir {JUGADOR_1}')
    elif JUGADOR_1 == 'invasor':
        print(f'el jugador 2 gana por elegir {JUGADOR_2}')
    else:
        print(f'error')
elif JUGADOR_1 == 'invasor' and JUGADOR_2 == 'rey' or JUGADOR_1 == 'rey' and JUGADOR_2 == 'invasor':
    
    if JUGADOR_1 == 'invasor':
        print(f'el jugador jugador 1 gana por elegir {JUGADOR_1}')
    elif JUGADOR_1 == 'rey':
        print(f'el jugador 2 gana por elegir {JUGADOR_2}')
    else:
        print(f'error')