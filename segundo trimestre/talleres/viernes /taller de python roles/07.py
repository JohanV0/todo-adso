general_1 = input('jugador 1:\nCual estrategia quiere usar? (atacar,defender,espiar): ').lower().strip()
general_1_intensidad = input('jugador 1:\nCual es tu nivel de intesidad (1 o 2): ')
general_2 = input('jugador 2:\nCual estrategia quiere usar? (atacar,defender,espiar): ').lower().strip()
general_2_intensidad = input('jugador 2:\nCual es tu nivel de intesidad (1 o 2): ')

movimientos_permitidos = 'atacar','defender','espiar'
comprobacion = general_1_intensidad == general_2_intensidad
ganador_por = None

if general_1 == general_2:
    ganador_por = 'empate'
    print(f'empate sin importar intensidad')

elif general_1 == "atacar" in movimientos_permitidos and general_2 == "espiar" in movimientos_permitidos:
    ganador_por = 'atacar jugador 1'
    print(f'\nel ganador es el jugador 1 por elegir {general_1} que le gana a {general_2} que eligio el jugador 2')

elif general_2 == "atacar" in movimientos_permitidos and general_1 == "espiar" in movimientos_permitidos:
    ganador_por = 'atacar jugador 2'
    print(f'\nel ganador es el jugador 2 por elegir {general_1} que le gana a {general_1} que eligio el jugador 1')

elif general_1 == "defender" in movimientos_permitidos and general_2 == "atacar" in movimientos_permitidos:
    ganador_por = 'defender jugador 1'
    print(f'\nel ganador es el jugador 1 por elegir {general_1} que le gana a {general_2} que eligio el jugador 2')

elif general_2 == "defender" in movimientos_permitidos and general_1 == "atacar" in movimientos_permitidos:
    ganador_por = 'defender jugador 2'
    print(f'\nel ganador es el jugador 2 por elegir {general_1} que le gana a {general_1} que eligio el jugador 1')

elif general_1 == "espiar" in movimientos_permitidos and general_2 == "defender" in movimientos_permitidos:
    ganador_por = 'espiar jugador 1'
    print(f'\nel ganador es el jugador 1 por elegir {general_1} que le gana a {general_2} que eligio el jugador 2')

elif general_2 == "defender" in movimientos_permitidos and general_1 == "espiar" in movimientos_permitidos:
    ganador_por = 'espiar jugador 2'
    print(f'\nel ganador es el jugador 2 por elegir {general_1} que le gana a {general_1} que eligio el jugador 1')
else:
    print(f'valores ingresados invalidos, solo valen (atacar,defender y espiar)')

if ganador_por == 'empate' and general_1_intensidad == general_2_intensidad:
    print(f'\nEs un empate total')
elif ganador_por == 'atacar jugador 1' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 1 gana por una victoria ajustada')

elif ganador_por == 'atacar jugador 1' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 1 gana por una vicotoria aplastante')

elif ganador_por == 'atacar jugador 2' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 2 gana por una vicotoria ajustada')

elif ganador_por == 'atacar jugador 2' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 2 gana por una vicotoria aplastante')

elif ganador_por == 'defender jugador 1' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 1 gana por una vicotoria ajustada')

elif ganador_por == 'defender jugador 1' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 1 gana por una vicotoria aplastante')

elif ganador_por == 'defender jugador 2' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 2 gana por una vicotoria ajustada')

elif ganador_por == 'defender jugador 2' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 2 gana por una vicotoria aplastante')

elif ganador_por == 'espiar jugador 1' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 1 gana por una vicotoria ajustada')

elif ganador_por == 'espiar jugador 1' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 1 gana por una vicotoria ajustada')

elif ganador_por == 'espiar jugador 1' and general_1_intensidad == '1' and general_2_intensidad == '2':
    print(f'\nEl jugador 2 gana por una vicotoria aplastante')

elif ganador_por == 'espiar jugador 1' and general_1_intensidad == '2' and general_2_intensidad == '1':
    print(f'\nEl jugador 2 gana por una vicotoria aajustada')
else:
    print(f'Error no se que')