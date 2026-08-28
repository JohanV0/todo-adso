#Las constantes necesarias son:
comprobacion = 'EMP'
intentos = 0
caracteres = 8


while not False:#Mientras no sea verdadero siga:
    codigo = input('Ingrese su codigo con las inciales EMP en el inicio: ')#Se guarda el codigo ingresado en la variable codigo
    intentos += 1 #Se aumenta el contador cuando se ingresa un codigo
    if comprobacion[0] == 'E' in codigo and comprobacion[1] == 'M' in codigo and comprobacion[2] == 'P' in codigo and len(codigo) == caracteres:#Para comprobar que el codigo si lleve EMP al inicio del codigo y lleva 8 caracteres
        print(f'Bienvenido, tu total de intentos fue: {intentos}')
        break
    elif comprobacion[0] == 'E' in codigo and comprobacion[1] == 'M' in codigo and comprobacion[2] == 'P' in codigo:#Se comprueba que lleva las iniciales EMP pero le falta la cantidad de caracteres
        print(f'El cogido le falta tener 8 caracteres')
    else:
        print('Error el codigo debe llevar EMP al inicio y 8 caracteres')#Si le hace falta todo
    