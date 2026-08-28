print('***Sistema De Administracion de Cuentas***')

salir = False

while not salir:
        print('''
    Menu:
        1.Crear Cuenta
        2.Elimiar Cuenta
        3.Sair
    ''')
        opcion = int(input('Escoge una opcion: (el numero):'))
        if opcion == 1:
            print('Creando tu cuenta...')
        elif opcion == 2:
            print('Eliminando tu cuenta...')
        elif opcion == 3:
            salir = True
            print('Saliendo del sistema. ¡Hasta pronto!')
        else:
             print('Error ingrese un valor valido')
else:
    print('Terminando el sistema de administracion de cuentas')