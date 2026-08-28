num = int(input('ingrese un numero ENTERO: '))
comprobacion = num % 2

if num > 0 and comprobacion == 0:
    print('el numero es positivo y es par')
elif num > 0 and comprobacion != 0:
    print('el numero es positivo y no es par')
elif num < 0 and comprobacion == 0:
    print('el numero es negativo y es par')
elif num < 0 and comprobacion != 0:
    print('el numero es negativo y es impar')
elif num == 0:
    print('el numero es cero')
else:
    print('error ingrese un valor valido')