def calcular_distancia_ruta(ruta):
    total = 0
    for tramo in ruta:
        total += tramo
    return total

def comparar_rutas(rutas):
    menor = None
    mejor = ""
    for nombre, ruta in rutas.items():
        distancia = calcular_distancia_ruta(ruta)
        if menor == None or distancia < menor:

            menor = distancia
            mejor = nombre
    return mejor

def calcular_tiempo_estimado(distancia, velocidad):
    return distancia / velocidad

def calcular_costo_combustible(distancia, rendimiento, precio):
    galones = distancia / rendimiento
    return galones * precio

rutas = {}
for i in range(3):
    nombre = input("Nombre ruta: ")
    cantidad = int(input("Cantidad de tramos: "))
    lista = []
    for j in range(cantidad):
        lista.append(float(input("Distancia tramo: ")))
    rutas[nombre] = lista

mejor = comparar_rutas(rutas)
distancia = calcular_distancia_ruta(rutas[mejor])
velocidad = float(input("Velocidad promedio: "))

print(f"""
Mejor ruta: {mejor}
print("Distancia:", distancia)
print("Tiempo:", calcular_tiempo_estimado(distancia, velocidad))
""")

rendimiento = float(input("Km por galón: "))
precio = float(input("Precio galón: "))
print("Costo combustible:", calcular_costo_combustible(distancia, rendimiento, precio))