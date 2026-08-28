#variables necesarias
salir = False
caracteres = 10
comienzo = '3'
intentos_fallidos = 0
comprobacion_numero = False
while not salir: #mientras no sea verdadero siga
    numero_telefonico = int(input('Digite su numero telefonico: '))#si es entero se guarda
    if len(str(numero_telefonico)) == caracteres and str(numero_telefonico)[0] == comienzo:#Si tiene 10 caracteres, comienza en 3 se muestra el mensaje de felicidades con los intetos
        comprobacion_numero = True
        print(f'Felicitaciones comprobacion exitosa. Intentos fallidos: {intentos_fallidos}')
        salir = True
    elif len(str(numero_telefonico)) != caracteres and str(numero_telefonico)[0] == comienzo:#si NO tiene 10 caracteres pero SI empieza por 3 se muestra el mensaje y aumenta el contador de intentos
        comprobacion_numero = False
        intentos_fallidos += 1
        print('El numero ingresado tiene que llevar 10 caracteres. Porfavor: ')
    elif len(str(numero_telefonico)) == caracteres and str(numero_telefonico)[0] != comienzo:#SI tiene 10 caracteres pero NO empieza por 3 se muestra el mensaje y aumenta el contador de intentos
        comprobacion_numero = False
        intentos_fallidos += 1
        print('El numero ingresado tiene que llevar "3" a inicio. Porfavor: ')
    else:
        intentos_fallidos += 1
        print('El numero ingresado debe llevar 10 numero y empezar con un "3". Porfavor: ')#si NO se cumple las condiciones necesarias se muestra el mensaje ya umenta el contador de intentos