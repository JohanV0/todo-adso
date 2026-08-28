nombre_usuario=input("Digite el nombre del usuario: ")
apellido_usuario=input("Digite el apellido del usuario: ")
año=int(input("Digite el nombre del usuario: "))

nombre_usuario_min=nombre_usuario.lower()
nombre_usuario_esp=nombre_usuario_min.replace(" ","")
apellido_usuario_min=apellido_usuario.lower()
apellido_usuario_esp=apellido_usuario_min.replace(" ","")
año=str(año)
concatenacion=nombre_usuario_esp+apellido_usuario_esp+año

print(f'El nombre del usuario es: {nombre_usuario_esp}')
print(f'el apellido del usuario es: {apellido_usuario_esp}')
print(f'el año de nacimiento es: {año}')
print(f'el nombre de usuario generado es: {concatenacion}')