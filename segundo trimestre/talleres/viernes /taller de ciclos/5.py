#variables necesarias
sofia = 0
miguel = 0
nulo = 0
salir = False

while not salir:#mientras no sea verdadero siga
    voto = input('Si desea votar por sofia, escriba "1".Si desea votar por miguel, escriba "2": ')#se gurada voto en la variable voto
    if voto == '1':# si voto es 1 se aumenta e contador de las variables de sofia
        sofia += 1
        salida = input('Desea salir? (n/terminar)').lower().strip()# si quiere salir o continuar, se guarda en la variable salida
        if salida == 'n':# si presiona n repita
            continue
        else:#Muestre si presiona terminar
            if sofia > miguel:
                ganador = sofia
            elif sofia < miguel:
                ganador = miguel
            else:
                ganador = 'empate'
            print(f'''
                Votos sofia: {sofia}
                Votos miguel: {miguel}
                Votos nulos: {nulo}
            ''')
            if ganador == sofia:
                print(f'ganador: {sofia} ')
            elif ganador == miguel:
                print(f'ganador: {miguel}')
            else:
                print(f'Empate tecnico')
            break
    elif voto == '2':# si voto es 2 se aumenta e contador de las variables de miguel
        miguel += 1
        salida = input('Desea salir? (n/terminar)').lower().strip()# si quiere salir o continuar, se guarda en la variable salida
        if salida == 'n':# si presiona n repita
            continue
        else:#Muestre si presiona terminar
            if sofia > miguel:
                ganador = sofia
            elif sofia < miguel:
                ganador = miguel
            else:
                ganador = 'empate'
            print(f'''
                Votos sofia: {sofia}
                Votos miguel: {miguel}
                Votos nulos: {nulo}
            ''')
            if ganador == sofia:
                print(f'ganador: {sofia} ')
            elif ganador == miguel:
                print(f'ganador: {miguel}')
            else:
                print(f'Empate tecnico')
            break
    else:
        nulo += 1# si voto es diferente a 1 o 2 se toma como nulo y aumenta el contaador
        salida = input('Desea salir? (s/terminar)').lower().strip()# si quiere salir o continuar, se guarda en la variable salida
        if salida == 'n':# si presiona n repita
            continue
        else:#Muestre si presiona terminar
            if sofia > miguel:
                ganador = sofia
            elif sofia < miguel:
                ganador = miguel
            else:
                ganador = 'empate'
            print(f'''
                Votos sofia: {sofia}
                Votos miguel: {miguel}
                Votos nulos: {nulo}
            ''')
            if ganador == sofia:
                print(f'ganador: {sofia} ')
            elif ganador == miguel:
                print(f'ganador: {miguel}')
            else:
                print(f'Empate tecnico')
            break
else:
    print('No se entro al sistema de votaciones.')