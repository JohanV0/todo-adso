jugador_1 = input('jugador 1:\nCual ser quiere usar? (alien,robot,humano): ')
jugador_2 = input('jugador 2:\nCual ser quiere usar? (alien,robot,humano): ')

movimientos_permitidos = 'alien','robot','humano'

if jugador_1 == 'alien' and jugador_2 == 'alien' :
    especial1 = input('jugador 1:\nSi desea activar la habilidad especial escriba "+especial sino desea, diga "no"').lower().strip() == '+especial'
    especial2 = input('jugador 2:\nSi desea activar la habilidad especial escriba "+especial"): ').lower().strip() == '+especial'
    if especial1 == True and especial2 == True:
        especial1 = jugador_1+'+especial'
        especial2 = jugador_2+'+especial'
        parsear_especial1 = especial1.replace('+especial','')
        parsear_especial2 = especial1.replace('+especial','')
        validar_base_1 = parsear_especial1 == 'alien'
        validar_base_2 = parsear_especial2 == 'alien'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {validar_base_2}')
        if validar_base_1 == True and validar_base_2 == True:
            print(f'Es un empate absoluto')
        else:
            print('La habilidad se debe activar con "+especial"')
    elif especial1 == True and especial2 == False:
        especial1 = jugador_1+'+especial'
        parsear_especial1 = especial1.replace("+especial","")
        print(parsear_especial1)
        validar_base_1 = parsear_especial1 == 'alien'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_1 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    elif especial1 == False and especial2 == True:
        especial2 = jugador_2+'+especial'
        parsear_especial2 = especial2.replace("+especial","")
        print(parsear_especial2)
        validar_base_2 = parsear_especial2 == 'alien'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_2}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_2 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    else:
        print('ningun jugador activo la habilidad especial')
elif jugador_1 == 'robot' and jugador_2 == 'robot':
    especial1 = input('jugador 1:\nSi desea activar la habilidad especial escriba "+especial sino desea, diga "no"').lower().strip() == '+especial'
    especial2 = input('jugador 2:\nSi desea activar la habilidad especial escriba "+especial"): ').lower().strip() == '+especial'
    if especial1 == True and especial2 == True:
        especial1 = jugador_1+'+especial'
        especial2 = jugador_2+'+especial'
        parsear_especial1 = especial1.replace('+especial','')
        parsear_especial2 = especial1.replace('+especial','')
        validar_base_1 = parsear_especial1 == 'robot'
        validar_base_2 = parsear_especial2 == 'robot'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {validar_base_2}')
        if validar_base_1 == True and validar_base_2 == True:
            print(f'Es un empate absoluto')
        else:
            print('La habilidad se debe activar con "+especial"')
    elif especial1 == True and especial2 == False:
        especial1 = jugador_1+'+especial'
        parsear_especial1 = especial1.replace("+especial","")
        print(parsear_especial1)
        validar_base_1 = parsear_especial1 == 'robot'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_1 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    elif especial1 == False and especial2 == True:
        especial2 = jugador_2+'+especial'
        parsear_especial2 = especial2.replace("+especial","")
        print(parsear_especial2)
        validar_base_2 = parsear_especial2 == 'robot'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_2}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_2 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    else:
        print('ningun jugador activo la habilidad especial')    
elif jugador_1 == 'humano' and jugador_2 == 'humano':
    especial1 = input('jugador 1:\nSi desea activar la habilidad especial escriba "+especial sino desea, diga "no"').lower().strip() == '+especial'
    especial2 = input('jugador 2:\nSi desea activar la habilidad especial escriba "+especial"): ').lower().strip() == '+especial'
    if especial1 == True and especial2 == True:
        especial1 = jugador_1+'+especial'
        especial2 = jugador_2+'+especial'
        parsear_especial1 = especial1.replace('+especial','')
        parsear_especial2 = especial1.replace('+especial','')
        validar_base_1 = parsear_especial1 == 'humano'
        validar_base_2 = parsear_especial2 == 'humano'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {validar_base_2}')
        if validar_base_1 == True and validar_base_2 == True:
            print(f'Es un empate absoluto')
        else:
            print('La habilidad se debe activar con "+especial"')
    elif especial1 == True and especial2 == False:
        especial1 = jugador_1+'+especial'
        parsear_especial1 = especial1.replace("+especial","")
        print(parsear_especial1)
        validar_base_1 = parsear_especial1 == 'humano'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_1}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_1 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    elif especial1 == False and especial2 == True:
        especial2 = jugador_2+'+especial'
        parsear_especial2 = especial2.replace("+especial","")
        print(parsear_especial2)
        validar_base_2 = parsear_especial2 == 'humano'
        print(f'el jugador 1 eligio: {jugador_1}, activo especial: {validar_base_2}')
        print(f'el jugador 2 eligio: {jugador_2}, activo especial: {especial2}')
        if validar_base_2 == True:
            print(f'el ganador es el jugador 1 por activar la especial')
    else:
        print('ningun jugador activo la habilidad especial')

elif jugador_1 == "alien" in movimientos_permitidos and jugador_2 == "robot" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "robot" in movimientos_permitidos and jugador_1 == "alien" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

elif jugador_1 == "robot" in movimientos_permitidos and jugador_2 == "humano" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "humano" in movimientos_permitidos and jugador_1 == "robot" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

elif jugador_1 == "humano" in movimientos_permitidos and jugador_2 == "alien" in movimientos_permitidos:
    print(f'el ganador es el jugador 1 por elegir {jugador_1} que le gana a {jugador_2} que eligio el jugador 2')

elif jugador_2 == "alien" in movimientos_permitidos and jugador_1 == "humano" in movimientos_permitidos:
    print(f'el ganador es el jugador 2 por elegir {jugador_1} que le gana a {jugador_1} que eligio el jugador 1')

else:
    print(f'valores ingresados invalidos, solo valen (roca,pergamino y garras)')