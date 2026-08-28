nombre_producto=input("Digite el nombre del producto: ")
categoria=input("Digite la categoria del producto: ")
año=input("Digite el año de lanzamiento: ")

nombre_producto_min=nombre_producto.lower()
nombre_producto_esp=nombre_producto_min.replace(" ","")
categoria_min=categoria.lower()
categoria_esp=categoria_min.replace(" ","")

concatenacion=nombre_producto_esp+'-'+categoria_esp+'-'+año

print(f'El nombre del producto es: {nombre_producto_esp}')
print(f'la categoria es: {categoria_esp}')
print(f'el año de lanzamiento es: {año}')
print(f'el nombre de codigo generado es: {concatenacion}')