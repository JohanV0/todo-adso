#Variables necesarias 
NUMER_SECRETO = 340
intentos = 5
intentos_fallidos = 0
numeros_arriba = 0
numeros_abajo = 0

while intentos != 0:
    adivina_numero = float(input('Adivina el numero secreto, digite el numero que cree: '))#Se pide y se guarda el valor ingresado por el usuario en la variable adivina_numero

    if adivina_numero > NUMER_SECRETO:#Si el numero es mayor al numero secreto se muestra un mensaje que se paso y se le resto 1 intento de 5 
        intentos -= 1
        intentos_fallidos += 1
        numeros_arriba += 1
        print('El numero ingresado es mayor al numero secreto')
        if intentos == 0:#Si se queda sin intentos se muestra el mensaje y se termina el codigo con el break
            print('Lo sentimos se acabaron los intentos.')
            break
        continue
    elif adivina_numero < NUMER_SECRETO:#Si el numero es menor al numero secreto se muestra un mensaje que se quedo corto y se le resto 1 intento de 5
        intentos -= 1
        intentos_fallidos += 1
        numeros_abajo += 1
        print('El numero ingresado es menor al numero secreto')
        if intentos == 0:#Si se queda sin intentos se muestra el mensaje y se termina el codigo con el break
            print('Lo sentimos se acabaron los intentos.')
            break
        continue
    elif adivina_numero == 0:#Si adivina el numero se muestra el mensaje con los intentos fallidos 
        print(f'Feicidades acertaste al numero.El numero era: {NUMER_SECRETO}. Intentos fallidos: {intentos_fallidos}')
        
