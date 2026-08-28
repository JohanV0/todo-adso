def asignar_turno(tecnicos, semana):
    posicion = (semana - 1) % len(tecnicos)
    return tecnicos[posicion]

def generar_calendario(tecnicos, semanas):
    calendario = []
    for semana in range(1, semanas + 1):
        calendario.append((semana, asignar_turno(tecnicos, semana)))
    return calendario

def contar_turnos_por_tecnico(calendario):
    conteo = {}
    for semana, tecnico in calendario:
        conteo[tecnico] = conteo.get(tecnico, 0) + 1
    return conteo

cantidad = int(input("Cantidad de técnicos: "))
tecnicos = []
for i in range(cantidad):
    nombre = input(f"Técnico {i+1} digite su nombre: ")
    tecnicos.append(nombre)

semanas = int(input("Cantidad de semanas: "))
calendario = generar_calendario(tecnicos, semanas)
print("CALENDARIO")

for semana, tecnico in calendario:
    print("Semana", semana, "->", tecnico)

print("Cantidad de turnos")
conteo = contar_turnos_por_tecnico(calendario)
for tecnico, cantidad in conteo.items():
    print(tecnico, ":", cantidad)