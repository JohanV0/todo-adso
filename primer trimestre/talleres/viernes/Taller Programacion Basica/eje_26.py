art1 = float(input('ingrese el valor del papel higienico: '))
art2 = float(input('ingrese el valor del jabon FAV: '))
art3 = float(input('ingrese el valor del Suavitel: '))
descuento = float(input('ingrese un descuento (en decimal, maximo 10%)'))
subtotal=art1+art2+art3
total_iva=subtotal*3
total=subtotal+total_iva
descuento = total * descuento
total_descuento = total + descuento

print(f'''
    subtotal: {subtotal}
    total con iva: {total_iva}
    total: {total}
    total con descuento: {total_descuento}''')