nombre="Andres Vergara"

minusculas = nombre.lower()
print(f"nombre en minusculas:'{minusculas}'")

espacio=minusculas.replace(" ", ".")
print(f'Espacio por puntos:{espacio}')

empresa= " ALPOSTO "

minusculas_empresa= empresa.lower()
print(f"Empresa en minusculas:'{minusculas_empresa}'")

nueva_cadena = minusculas_empresa.replace(" ","")
print(f"sin espacios:'{nueva_cadena}'")

dominio=".com.al"

correo=espacio+"@"+nueva_cadena+dominio
print(correo)