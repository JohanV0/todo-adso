nombre = input('Digite su nombre: ').strip().title()
año = input('Digite su año de nacimiento: ').strip()

letras_nombre = nombre [0:2]
letras_año = año [2:4]
largo_nom = len(nombre)
print(f'{letras_nombre}{letras_año}{largo_nom}')