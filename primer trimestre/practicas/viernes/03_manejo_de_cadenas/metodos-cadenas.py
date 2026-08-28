#Metodos de cadenas
cadena1 = 'Hola Mundo'
print(f'Cadena original:{cadena1}')

#Convierte a mayusculas usando upperr()
mayusculas = cadena1.upper()
print(f'cadena en mayusculas:{mayusculas}')

#Convierte a minusculas usando lower()
minusculas = cadena1.lower()
print(f'cadena en minusculas:{minusculas}')

#Elimina espacios al inicio y al final usando strip()
cadena2 = " juan perez "
print(f'cadena con espacios:{cadena2}')
cadena_sin_espacios = cadena2.strip()
print(f'Cadena sin  espacios:"{cadena_sin_espacios}"')

#Coloca la primera en mayuscula utiliznado title()
cadena3 = 'hola mundo'
print(f'Cadena original:{cadena3}')

cadena_la_primera_mayuscula = cadena3.title()
print(f'Cadena con la primera en mayusculas:{cadena_la_primera_mayuscula}')

#Remplaza caracteres usando replace('a','o')
caracteres = cadena1.replace('o','a')
print(f'remplaza caracteres o por a:{caracteres}')

