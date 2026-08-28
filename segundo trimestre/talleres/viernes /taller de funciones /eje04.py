def clasificar_turno(hora):
    if hora.isdigit() == False:
        return 'Hora invalida, debe de ser entre (0,23)'
    else:
        hora = int(hora)
        if hora >= 0 and hora <= 23:
            if hora >= 6 and hora <= 11:
                return f'Su turno es de mañana'
            elif hora >= 12 and hora <= 17:
                return f'Su turno es de tarde'
            else:
                return f'Su turno es de noche'
hora = input('Digite su hora de ingreso: ')
print(clasificar_turno(hora))