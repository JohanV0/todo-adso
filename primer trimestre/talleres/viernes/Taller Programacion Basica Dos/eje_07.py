precio = float(input('digite el precio del producto: '))
cantidad = float(input('digite la cantidad de producto a llevar: '))
precio2 = float(input('digite el precio del nuevo producto: '))
cantidad2 = float(input('digite la cantidad del nuevo productoa llevar: '))

total = (precio * cantidad) + (precio2 * cantidad2)
comprobacion = total > 100000

print(f'el total de los productos supera el limite de 100000?: {comprobacion}')