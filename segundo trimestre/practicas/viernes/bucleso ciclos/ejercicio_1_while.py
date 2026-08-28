max = 5
num = 1
acumulado_suma = 0

while  num <=  max:
    print(f'acumulador + numero {acumulado_suma} + {num}')
    acumulado_suma += num
    num += 1
    if acumulado_suma != 15:
        print(f'suma parcial: {acumulado_suma}')
    else:
        print(f'suma total: {acumulado_suma}')