print('Cajero automatico')

SALDO = 100000
SALIR = False

while not SALIR:
        print('''
    Menu:
        1.Consultar Saldo
        2.Retirar
        3.Depositar
        4.Salir
    ''')
        opcion = int(input('Porfavor Seleccione una opcion:'))
        if opcion == 1:
            print(f'Tu saldo actual es: {SALDO}')
        elif opcion == 2:
            retirar = float(input(f'Ingrese monto a retirar: '))
            SALDO -= retirar
            print(f'Su saldo actual es: {SALDO}')
        elif opcion == 3:
            depositar = float(input(f'Ingrese monto a depositar: {SALDO}'))
            SALDO += depositar
            print(f'Su saldo actual es: {SALDO}')
        elif opcion == 4:
            SALIR = True
            print('Saliendo del Cajero Automatico. ¡Hasta pronto!')
        else:
             print('Error ingrese un valor valido')
else:
    print('Terminando el sistema de Cajero Automatico')