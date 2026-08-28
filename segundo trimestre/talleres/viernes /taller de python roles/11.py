ronda_1_jugador = input('jugador 1 elija su opcion (piedra, papel o tijeras): ')
maquina = 'papel'
puntos = 0
ronda = 0
if ronda_1_jugador == maquina:
    puntos += 1
    ronda = 1
    print(f'Ronda {ronda}: Tu elegiste: {ronda_1_jugador} vs Maquina eligio: {maquina} = empate')
    ronda_2_jugador = input('jugador elija su opcion (piedra, papel o tijeras) para desempatar: ')
    maquina = 'tijera'  
    if ronda_2_jugador == maquina:
        puntos += 1
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'piedra':
        puntos += 3
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'papel':
        puntos += 0
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
elif ronda_1_jugador == 'tijera':
    puntos += 3
    ronda = 1
    print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
    ronda_2_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
    maquina = 'tijera'  
    if ronda_2_jugador == maquina:
        puntos += 1
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'piedra':
        puntos += 3
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'papel':
        puntos += 0
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
elif ronda_1_jugador == 'piedra':
    puntos += 0
    ronda = 1
    print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
    ronda_2_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
    maquina = 'tijera'  
    if ronda_2_jugador == maquina:
        puntos += 1
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'piedra':
        puntos += 3
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')
    elif ronda_2_jugador == 'papel':
        puntos += 0
        ronda = 2
        print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
        ronda_3_jugador = input('jugador elija su opcion (piedra, papel o tijeras): ')
        maquina = 'piedra'  
        if ronda_3_jugador == maquina:
            puntos += 1
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'piedra':
            puntos += 3
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        elif ronda_3_jugador == 'papel':
            puntos += 0
            ronda = 1
            print(f'Ronda {ronda}: Tu {ronda_1_jugador} vs Maquina {maquina} = empate')
            print(f'finalizo con un total de {puntos} puntos -> Puntaje >= 3: Campeon  |  1-2: Competente  |  0: Novato')
        else:
            print('valores ingresados incorrectos')