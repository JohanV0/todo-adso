def calcular_afinidad(cliente1, cliente2):
    return len(cliente1.intersection(cliente2))

def cliente_mas_afin(clientes, cliente_objetivo):
    mayor = -1
    mejor = ""
    for cliente, productos in clientes.items():
        if cliente != cliente_objetivo:
            afinidad = calcular_afinidad(clientes[cliente_objetivo], productos)
            if afinidad > mayor:
                mayor = afinidad
                mejor = cliente
    return mejor

def recomendar_productos(clientes, cliente_objetivo, cliente_afin):
    return clientes[cliente_afin] - clientes[cliente_objetivo]

def porcentaje_afinidad(cliente1, cliente2):
    comun = len(cliente1.intersection(cliente2))
    union = len(cliente1.union(cliente2))
    if union == 0:
        return 0
    return (comun / union) * 100

clientes = {}
cantidad = 4

for i in range(cantidad):
    nombre = input("Nombre del cliente: ")
    productos = input("Productos separados por coma: \n")
    clientes[nombre] = set(productos.split(","))
objetivo = input("Cliente objetivo: ")
afin = cliente_mas_afin(clientes, objetivo)

print(f"""
Cliente más afín: {afin}
Productos recomendados: {recomendar_productos(clientes, objetivo, afin)}
Porcentaje de afinidad: {porcentaje_afinidad(clientes[objetivo], clientes[afin])}%
""")