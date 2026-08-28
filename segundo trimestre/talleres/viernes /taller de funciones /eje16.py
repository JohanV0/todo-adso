def registrar_cliente(cola, nombre):
    cola.append(nombre)
    return cola

def atender_cliente(cola):
    if len(cola) == 0:
        return None, cola
    cliente = cola.pop(0)
    return cliente, cola

def atender_siguiente(cola):

    for i in range(len(cola)):
        nombre, prioridad = cola[i]
        if prioridad == "urgente":
            return cola.pop(i), cola
    return cola.pop(0), cola

cantidad = int(input("Cantidad de clientes: "))
cola = []

for i in range(cantidad):
    nombre = input("Nombre: ")
    prioridad = input("Prioridad (normal/urgente): ")
    registrar_cliente(cola, (nombre, prioridad))

print("\nATENCIÓN\n")
while len(cola) > 0:
    cliente, cola = atender_siguiente(cola)
    
    print(f"""
Atendido: {cliente[0]}
Prioridad: {cliente[1]})
Pendientes: {len(cola)})
""")