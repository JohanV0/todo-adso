def generar_tarjeta(nombre, cargo,ciudad,jornada = "Diurno"):
    if jornada == "":
        jornada = "Diurno"
    else:
        jornada = jornada
    return f"Nombre: {nombre} | Cargo: {cargo} | Ciudad: {ciudad} | Turno: {jornada}"
nombre = input('Digite su nombre completo: ').lower()
cargo = input('Digite su cargo en la empresa: ').strip().lower()
ciudad = input('Lugar de residiencia: ').strip().lower()
jornada = input('Digite su jornada (si ya tiene asignada): ')
print(generar_tarjeta(nombre,cargo,ciudad,jornada))
