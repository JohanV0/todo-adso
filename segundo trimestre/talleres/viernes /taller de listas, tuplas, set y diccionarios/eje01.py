productos = ["Laptop HP","Mouse Logitech","Disco SSD","Laptop HP","Teclado Redragon","Monitor LG","Mouse Logitech","Laptop HP","Disco SSD","Teclado Redragon","Monitor LG","Laptop HP","Cable HDMI","Mouse Logitech","Monitor LG"]#Se crea la lsta de productos

productos_sin_duplicado = list(set(productos))#se convierte la lista a set para sacar duplicados y se devuelve a lista

conteo_productos = {} #se crea un diccionario vacio donde se va a guardar la cantidad de cada producto
for contar_productos in productos:

    conteo_productos[contar_productos] = conteo_productos.get(contar_productos,0)+1#si esta la clave ya, se aumenta el valor y no se duplica la llave

mayor_valor = int(max(conteo_productos.values()))#se saca el maximo de los valores y se convierte en entero
suma = sum(conteo_productos.values()) #se suman todos los valores del diccionario
porcentaje = (mayor_valor / suma) * 100 #se saca el porcentaje del producto mayor 
top3_productos = tuple(sorted(conteo_productos.items(), key = lambda x: x[1], reverse=True))#Se organiza el diccionario por el indice 1 de manera descendente y se convierte en tupla

#se muestran los valores 
print(f'''
      Productos:
      {productos_sin_duplicado}
      Cantidad de productos:
      {conteo_productos}
      Prodcuto mas vendido:
      {max(conteo_productos.items(), key = lambda x: x[1])}
      Porcentaje del producto mas vendido:
      {porcentaje:.2f}%
      top 3 productos:
      {top3_productos[0:3]}
      ''')

