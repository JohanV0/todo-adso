print('***Creacion y Validacion de un Password***')

SALIR = False
CARACTERES = 6
password = input('ingrese su contraseña: ')
while len(password) <= CARACTERES:
    print('El password no cumple los requisitos. Debe tener al menos 6 caracteres')
    salida = input('Si desea continuar ingrese 1, si desea salir presione 0: ')
    password = input('Ingrese un nuevo valor de password: ')
    if len(password) == CARACTERES:
        print('El valor de password es valido')
    salida = input('Presione 0 para salir: ')
    if salida == '0':
        SALIR = True
        print('\nSaliendo de la validacion')
    else:
        print('Password correcto porfavor presione 0 para terminar')
else:
    print('Gracias por usar nuestra validacion')