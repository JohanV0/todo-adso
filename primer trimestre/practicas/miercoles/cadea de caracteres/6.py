nombre = "Minch Yoda"
trabajo = "Star Wars"
planeta = "Tatton \t cinco"
vacia = ""
print(len(nombre))
print(len(trabajo))
print(len(planeta))
print(len(vacia))

gerente = input('ingrese el nombre de gerente de grado: ').strip().lower()
coordinadora = input('ingrese el nombre de la coordinadora de grado: ').strip().lower()
nombre = input('ingrese el nombre de mio: ').strip().lower()
nombre_compa = input('ingrese el nombre de un compañero: ').strip().lower()

print(f'''
    el nombre del gerente de grado tiene: {len(gerente)} caracteres
    el nombre de la coordinadora tiene: {len(coordinadora)} caracteres
    el nombre suyo tiene: {len(nombre)} caracteres
    el nombre del compañero tiene: {len(nombre_compa)} caracteres
''')

