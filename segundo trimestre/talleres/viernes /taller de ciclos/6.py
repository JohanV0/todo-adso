#variables necesarias
salir = False
intentos_maximos = 3
intentos = 0
intentos_exitosos = 0
limite_caracteres = 4
while not salir: #Mientras no sea verdadero siga
    clave = str(input('Ingrese su clave numerica: '))#Se guarda la clave en la variable clave
    if len(clave) > limite_caracteres:#Se comprueba el limite de caracteres si es verdad o no 
        intentos += 1
        intentos_maximos -= 1
        if intentos_maximos == 0:#Si llega al limite maximo muestra el mensaje
            print('Dispositivo Bloqueado')
        else:
            continue
        print(f'''
Clave incorrecta. Intentos disponibles: {intentos_maximos}
intentos fallidos: 3
intentos exitosos: {intentos_exitosos}
''')#Cuando se quede sin intentos muestra el mensaje
        break

    elif len(clave) <= limite_caracteres:#Si cumple con las caracteres muestra mensaje
        intentos +=1
        intentos_exitosos += 1
        print('Dispositivo desbloqueado')
else:
    print('no entro al programa')#Si se termina o no inicia el programa
