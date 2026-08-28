RANGO_MIN = 1
RANGO_MAX = 100
numero=int(input('ingrese un valor entero: '))
numero = numero >= RANGO_MIN and numero <= RANGO_MAX
print(f'Valor dentro del rango: {numero}')