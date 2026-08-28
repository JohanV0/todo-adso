nombre=input("digite el nombre completo: ")
apellido=input("digite el apellido completo: ")
empresa=input("digite el nombre de la empresa:")
extension=".co"

nombre_mod=nombre.strip().lower().replace(" ","")
apellido_mod=apellido.strip().lower().replace(" ","")
empresa_mod=empresa.strip().lower().replace(" ","")
concatenacion=nombre_mod+apellido_mod+"@"+empresa_mod+extension

print(f'el nombre del usuario modificado: {nombre_mod}')
print(f'el apellido del usuario modificado: {apellido_mod}')
print(f'la extension modificada es: {empresa_mod}')
print(f'correo generado es: {concatenacion}')