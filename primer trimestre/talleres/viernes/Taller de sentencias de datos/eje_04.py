compra = float(input('Ingrese la cantidad de compra: '))

if compra > 500000:
    descuento = compra * 0.1
    total = compra - descuento
    print(f'Por su compra de {compra}, su descuento es de: {descuento}, con el pago final de: {total}')
elif compra >= 200000 and compra <= 500000:
    descuento = compra * 0.05
    total = compra - descuento
    print(f'Por su compra de {compra}, su descuento es de: {descuento}, con el pago final de: {total}')
else:
    print(f'Por su compra de {compra}, no cumple con descuento')
