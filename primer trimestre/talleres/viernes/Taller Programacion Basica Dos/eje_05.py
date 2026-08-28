nombre = input('Digite su nombre: ').strip().title()
edad = int(input('Digite su edad actual: '))

letras_nombre = nombre [-1]
edad = edad * 2
largo_nom = len(nombre)
print(f'{letras_nombre}{edad}{largo_nom}')