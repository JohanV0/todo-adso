art1 = float(int('ingrese el valor del papel higienico: '))
art2 = float(int('ingrese el valor del jabon FAV: '))
art3 = float(int('ingrese el valor del Suavitel: '))

subtotal=art1+art2+art3
total_iva=subtotal*3
total=subtotal+total_iva

print(f'''
    subtotal: {subtotal}
    total con iva: {total_iva}
    total: {total}''')