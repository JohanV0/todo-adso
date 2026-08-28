peso = float(input('Ingrese el peso del paquete: '))

if peso < 5:
    total = peso * 15000
    print(f'El costo total de envio es de: {total}: ')
elif peso > 5 and peso < 15:
    total = peso * 12000
    print(f'El costo total de envio es de: {total}')
else:
    total = peso * 10000
    print(f'El costo total de envio es de {total}')
