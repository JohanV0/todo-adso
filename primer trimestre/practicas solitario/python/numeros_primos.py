num = int(input("digite su numero: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("el numero ingresado no es primo")
            break
    else:
        print("el numero ingresado es primo")
else:
    print('ingrese un numero valido')
    