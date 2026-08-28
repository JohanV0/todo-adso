fecha_uno = input(f'Digite una fecha en formato (Dia/Mes): ')
fecha_dos = input(f'Digite otra fecha con formato (Dia/Mes)')

if fecha_uno > fecha_dos:
    print(f'la fecha {fecha_uno} es mayor a {fecha_dos}')
elif fecha_uno < fecha_dos:
    print(f'la fecha {fecha_uno} es menor a {fecha_dos}')
elif fecha_uno == fecha_dos:
    print(f'la fecha {fecha_uno} es igual a {fecha_dos}')
else:
    print(f'error digite una fecha valida')