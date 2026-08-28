
asistencias = {
    "Ana": 92,
    "Luis": 78,
    "María": 85,
    "Carlos": 74,
    "Sofía": 88,
    "Pedro": 69,
    "LAura": 95,
    "Juan": 82,
    "Valentina": 76,
    "Diego": 50,
}
# Categorías
excelente = [n for n, p in asistencias.items() if p > 85]
en_riesgo = [n for n, p in asistencias.items() if 75 <= p <= 85]
sin_derecho = [n for n, p in asistencias.items() if p < 75]

print("Persona con asistencia excelente (mas de 85%):", excelente)
print("Personas en riesgo (entre 75% - 85%):", en_riesgo)
print("Personas sin derecho (menos de 75%):", sin_derecho)

# Sacar el promedio 
promedio = sum(asistencias.values()) / len(asistencias)
print(f"\nPromedio general de asistencia: {promedio:.2f}%")

# Diccionario de estado_asistencia
estado_asistencia = {}
for nombre, porcentaje in asistencias.items():
    if porcentaje > 85:
        estado_asistencia[nombre] = porcentaje
    elif porcentaje >= 75 and porcentaje <= 85:
        estado_asistencia[nombre] = porcentaje
    else:
        estado_asistencia[nombre] = porcentaje

print('-'*120)
for j,c in sorted(estado_asistencia.items(), key = lambda x: x[1], reverse=True):
    if c > 85:
        print(f'- {j} -> ESTA HABILITADO')
    elif c <= 85 and c >= 75:
        print(f'- {j} -> EN RIESGO')
    else:
        print(f'- {j} -> SIN DERECHO')
