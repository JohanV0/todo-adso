#se guardar los datos en una tupla
inventario = ("Laptop HP","Mouse Logitech","Disco SSD","Teclado Redragon","Monitor LG","Cable HDMI","PC","Router Asus","Camara Web","Switch")

pedido = ["Laptop HP","Tablet Samnsung","Monitor LG","UPS APC","Mouse Logitech","Impersora Epson"] #se hace el pedido con una lista 

pedido_disponibles = () #se guarda los pedidos disponibles en una tupla
pedido_no_disponibles = () #se guarda los pedidos NO dispinibles en una tupla 

for producto in pedido:
    if producto in inventario:
        pedido_disponibles.append(producto) #se agrega el prodcuto que si esta en la lista de inventario a la tupla de pedidos disponibles
    else:
        pedido_no_disponibles.append(producto) #se agrega el producto que no esta en la lista de inventario a la tupla de pedidos disponibles 
print(f'Productos disponibles: {pedido_disponibles}') #se muestran los productos
print(f'Productos NO disponibles: {pedido_no_disponibles}')
        
porcentaje_de_cumplimiento = (len(pedido_disponibles) / len(pedido)) * 100 #se saca el porcentaje de cumplimiento 
print(porcentaje_de_cumplimiento) #se imprime el porcentaje de rendimiento 

simulacion_de_cumplimiento_total = tuple(list(pedido_disponibles +pedido_no_disponibles)) #se hace la simulacion del 100% del pedido y se convierte de lista a tupla 
print(simulacion_de_cumplimiento_total)#se imprime la simulacion 