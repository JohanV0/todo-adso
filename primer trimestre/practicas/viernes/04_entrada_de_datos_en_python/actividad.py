
from random import randint
nombre=str(input("digite su nombre: "))
apellido=str(input("digite su apellido: "))
año=int(input("digite su año de nacimiento: "))
num=randint(1000,9999)

nombre=nombre.strip().replace(" ","")

subnombre = nombre.upper().strip().replace(" ","")
sub_nombre = subnombre[0:2]
subapellido= apellido.upper().strip().replace(" ","")
sub_apellido = subapellido[0:2]
año_str=str(año).strip().replace(" ","")
sub_año=año_str[2:4]

print(f'Bienvenido: {nombre} al servicio nacional de aprendizaje \n su correo generado es de:{sub_nombre}{sub_apellido}{sub_año}{num}')