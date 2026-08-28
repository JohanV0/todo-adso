jugador_1 = input('jugador 1:\nCual magia quiere usar? (Roca,Pergamino,Garras): ')
jugador_2 = input('jugador 2:\nCual magia quiere usar? (Roca,Pergamino,Garras): ')

movimientos_permitidos = 'roca','pergamino','garras'

if jugador_1 == "roca" in movimientos_permitidos and jugador_2 == "roca" in movimientos_permitidos:
    poder_roca1 = float(input('jugador 1:\nDigita tu nivel de poder de (1 a 100): '))
    poder_roca2 = float(input('jugador 2:\nDigita tu nivel de poder de (1 a 100): '))
    if poder_roca1 > poder_roca2:
        print(f'El ganador es el jugador 1')
    elif poder_roca1 < poder_roca2:
        print(f'El ganador es el jugador 2')
    elif poder_roca1 == poder_roca2:
        print(f'Es un empate absoluto de los dos jugadores')
    else:
        print(f'Error el valor ingresado no es un numero')
elif jugador_1 == "roca" in movimientos_permitidos and jugador_2 == "garras" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "roca" in movimientos_permitidos and jugador_1 == "garras" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

elif jugador_1 == "pergamino" in movimientos_permitidos and jugador_2 == "roca" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "pergamino" in movimientos_permitidos and jugador_1 == "roca" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

elif jugador_1 == "garras" in movimientos_permitidos and jugador_2 == "pergamino" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "pergamino" in movimientos_permitidos and jugador_1 == "garras" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

else:
    print(f'valores ingresados invalidos, solo valen (roca,pergamino y garras)')