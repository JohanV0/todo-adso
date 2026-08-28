def encontrar_duplicados(lista):
    vistos = set()
    duplicados = set()

    for cedula in lista:
        if cedula in vistos:
            duplicados.add(cedula)
        else:
            vistos.add(cedula)

    return duplicados


def eliminar_duplicados_preservando_orden(lista):
    nueva = []
    vistos = set()

    for cedula in lista:
        if cedula not in vistos:
            nueva.append(cedula)
            vistos.add(cedula)

    return nueva


def contar_apariciones(lista):
    conteo = {}

    for cedula in lista:
        conteo[cedula] = conteo.get(cedula, 0) + 1

    ordenado = dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))
    return ordenado


cantidad = int(input("Cantidad de cédulas: "))

cedulas = []

for i in range(cantidad):
    cedulas.append(input(f"Cédula {i+1}: "))

print(f"""
Duplicados: {encontrar_duplicados(cedulas)}
Lista sin duplicados:{eliminar_duplicados_preservando_orden(cedulas)})
Apariciones: {contar_apariciones(cedulas)})
""")