def calcular_promedio_evaluacion(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excepcional"
    elif promedio >= 4:
        return "Sobresaliente"
    elif promedio >= 3:
        return "Satisfactorio"
    else:
        return "En mejora"

def generar_reporte_colaborador(nombre, notas):
    promedio = calcular_promedio_evaluacion(notas)
    categoria = clasificar_desempeño(promedio)
    return {
        "nombre": nombre,
        "promedio": promedio,
        "categoria": categoria
    }

def generar_reporte_general(reportes):
    mejor = ""
    mayor = -1
    categorias = {
        "Excepcional":0,
        "Sobresaliente":0,
        "Satisfactorio":0,
        "En mejora":0
    }

    for reporte in reportes:
        if reporte["promedio"] > mayor:
            mayor = reporte["promedio"]
            mejor = reporte["nombre"]
        categorias[reporte["categoria"]] += 1
    return mejor, categorias

def identificar_en_riesgo(reportes):
    riesgo = []
    for reporte in reportes:
        if reporte["categoria"] == "En mejora":
            riesgo.append(reporte["nombre"])
    return riesgo

reportes = []

while True:
    nombre = input("Nombre (salir para terminar): ")
    if nombre.lower() == "salir":
        break
    notas = input("Notas separadas por coma: ")
    lista = []
    for nota in notas.split(","):
        lista.append(float(nota))
    reporte = generar_reporte_colaborador(nombre, lista)
    reportes.append(reporte)
    print(reporte)
mejor, categorias = generar_reporte_general(reportes)

print(f"""
Mejor colaborador: {mejor}
Categorías: {categorias})
En riesgo: {identificar_en_riesgo(reportes)}
""")