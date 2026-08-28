cantidad_compra=int(input('ingrese la cantidad de elementos a comprar: ').lower().strip() == 5)
membresia = bool(input('tiene membresia? ' ).lower().strip() == 'si')

descuento = cantidad_compra == 5 and membresia == 'si'
print(f'''
    Cumple conn las condiciones para el prestamo de un libro? {descuento}''')