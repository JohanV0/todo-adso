nombre_profesor=input("Digite el nombre del profesor: ")
apellido_profesor=input("Digite el apellido del profesor: ")
materia=input("Digite materia de enseñanza: ")
colegio="lcgs"
dominio=".edu.co"

nombre_profesor_min=nombre_profesor.lower()
nombre_profesor_esp=nombre_profesor_min.replace(" ","")
apellido_profesor_min=apellido_profesor.lower()
apellido_profesor_esp=apellido_profesor_min.replace(" ","")
materia_min=materia.lower()
materia_esp=materia_min.replace(" ","")


concatenacion=nombre_profesor_esp+apellido_profesor_esp+'@'+materia_esp+colegio+dominio

print(f'El nombre del profesor es: {nombre_profesor_esp}')
print(f'el apellido del profesor es: {apellido_profesor_esp}')
print(f'la materia de enseñanza es: {materia_esp}')
print(f'el correo generado es: {concatenacion}')