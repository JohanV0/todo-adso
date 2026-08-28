compra = float(input('Ingrese la cantidad de compra: '))
miembro = input('Usted es miembro de la tienda?: ').strip().lower()

if compra > 1000 and miembro == "si":
    descuento = compra * 0.10
    total = compra - descuento
    print(f'Por ser miembro y tener una compra de mas de {compra}, su descuento es de: {descuento}, con el pago final de: {total}')
elif miembro == 'si' :
    descuento = compra * 0.10
    total = compra - descuento
    print(f'Por ser miembro, su descuento es de: {descuento}, con el pago final de: {total}')
else:
    descuento = compra * 0.0
    total = compra - descuento
    print(f'SU compra final es de: {total}')