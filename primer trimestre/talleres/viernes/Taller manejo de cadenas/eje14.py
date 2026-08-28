nombre_empleado=input("Digite el nombre del empleado: ")
apellido_empresa=input("Digite el apellido de la empresa: ")
departamento=input("Digite el departamento: ")

nombre_empleado_min=nombre_empleado.lower()
nombre_empleado_esp=nombre_empleado_min.replace(" ","")
apellido_empresa_min=apellido_empresa.lower()
apellido_empresa_esp=apellido_empresa_min.replace(" ","")
departamento_min=departamento.lower()
departamento_esp=departamento_min.replace(" ","")
empresa="sena"

concatenacion=nombre_empleado_esp+apellido_empresa_esp+'@'+departamento_esp+empresa+'.com'

print(f'El nombre del empleado es: {nombre_empleado_esp}')
print(f'el apellido del empleado es: {apellido_empresa_esp}')
print(f'el departamento es: {departamento_esp}')
print(f'el correo generado es: {concatenacion}')