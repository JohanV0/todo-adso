
# Diccionario de notas (calificaciones)
calificaciones = {
    'Ana': 4.5, 
    'Luis': 3.8, 
    'María': 4.9, 
    'Carlos': 2.7, 
    'Sofía': 2.2, 
    'Pedro': 4.1, 
    'Laura': 3.2, 
    'Juan': 4.7, 
    'Valentina': 2.9, 
    'Diego': 3.6
}

# Diccionario de asistencias (porcentajes)
asistencias = {
    "Ana": 92,
    "Luis": 78,
    "María": 85,
    "Carlos": 74,
    "Sofía": 88,
    "Pedro": 69,
    "Laura": 95,
    "Juan": 82,
    "Valentina": 76,
    "Diego": 50,
}

# Lista de aprendices que cumplen AMBAS condiciones: nota >= 4.0 y asistencia > 85%
destacados = [
    n for n in calificaciones and asistencias
    if calificaciones[n] >= 4.0 and asistencias[n] > 85
]
print(destacados)
parcial = [
    n for n in calificaciones and asistencias
    if calificaciones[n] >= 4.0 != asistencias[n] > 85
]
print(parcial)
no_cumple = [
    n for n in calificaciones and asistencias
    if calificaciones[n] < 4.0 and asistencias[n] <= 85
]
print(no_cumple)

puntajes = {
}
for n in calificaciones and asistencias:
    nota = calificaciones[n]
    asistencia = asistencias[n]
    puntajes[n] = (nota * 0.4) + (asistencia * 0.4 * 5)

ranking_3 = sorted(puntajes.items(), key=lambda x: x[1], reverse= True)

print(dict(ranking_3[0:3]))