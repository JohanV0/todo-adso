# Resumen final de resultados por grupo de estudio

grupos = {
    "Programacion": [4.2, 3.9, 4.5, 3.1, 3.8, 4.0],
    "DiseñoWeb": [3.0, 2.7, 3.4, 4.0, 3.6, 3.2],
    "Analitica": [4.9, 4.7, 4.8, 4.3, 4.1, 4.6],
    "Redes": [2.8, 3.0, 2.6, 3.2, 3.1, 2.9],
}

from statistics import mean

# aquí se guardará el promedio de cada grupo
resultado_promedios = {}

# aquí se guardará la cantidad de estudiantes aprobados
cantidad_aprobados = {}

# aquí se guardará la cantidad de estudiantes reprobados
cantidad_reprobados = {}

# aquí se guardará la dispersión de las notas de cada grupo
nivel_variacion = {}

# se recorren todos los grupos junto con sus notas
for nombre_grupo, lista_notas in grupos.items():

    # se calcula el promedio del grupo
    promedio_grupo = mean(lista_notas)

    # se guarda el promedio redondeado a tres decimales
    resultado_promedios[nombre_grupo] = round(promedio_grupo, 3)

    # cuenta cuántas notas son mayores o iguales a 3
    cantidad_aprobados[nombre_grupo] = sum(1 for nota in lista_notas if nota >= 3.0)

    # cuenta cuántas notas son menores a 3
    cantidad_reprobados[nombre_grupo] = sum(1 for nota in lista_notas if nota < 3.0)

    # calcula qué tan alejadas están las notas del promedio
    diferencia_promedio = mean([abs(nota - promedio_grupo) for nota in lista_notas])

    # guarda el resultado redondeado
    nivel_variacion[nombre_grupo] = round(diferencia_promedio, 3)

# muestra los promedios de cada grupo
print("Promedio obtenido por cada grupo:")

for nombre_grupo, promedio in resultado_promedios.items():
    print(f" - {nombre_grupo}: {promedio:.3f}")

# busca el grupo con mejor promedio
grupo_destacado = max(resultado_promedios.items(), key=lambda dato: dato[1])

# busca el grupo con menor promedio
grupo_bajo = min(resultado_promedios.items(), key=lambda dato: dato[1])

print()
print(f"Grupo con mejor promedio: {grupo_destacado[0]} con {grupo_destacado[1]:.3f}")
print(f"Grupo con menor promedio: {grupo_bajo[0]} con {grupo_bajo[1]:.3f}")

# muestra cuántos aprobaron y reprobaron en cada grupo
print("\nCantidad de aprobados y reprobados por grupo:")

for nombre_grupo in grupos:
    print(
        f" - {nombre_grupo}: "
        f"{cantidad_aprobados[nombre_grupo]} aprobaron y "
        f"{cantidad_reprobados[nombre_grupo]} reprobaron"
    )

# muestra la dispersión de las notas de cada grupo
print("\nNivel de variación de las notas por grupo:")

for nombre_grupo, variacion in nivel_variacion.items():
    print(f" - {nombre_grupo}: {variacion:.3f}")

# encuentra el grupo donde las notas están más separadas entre sí
grupo_mas_variable = max(nivel_variacion.items(), key=lambda dato: dato[1])

print()
print(
    f"Grupo con mayor variación en sus notas: "
    f"{grupo_mas_variable[0]} con valor {grupo_mas_variable[1]:.3f}"
)