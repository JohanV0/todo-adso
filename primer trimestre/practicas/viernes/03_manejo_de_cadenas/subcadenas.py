#Manejo de subcadenas
cadena = 'Hola Mundo'

# Obetener una subcadena desde el inicio hasta la posicion 4 sin incluirla
subcadena_hola = cadena [0:4]
print(f'Subcadena de hola: {subcadena_hola}')

subcadena_mundo = cadena [5:10]
print(f'Subcadena de mundo: {subcadena_mundo}')

texto= "HOLA MUNDO"
letras= "HAUO" # Definimos otra cadena que contiene las letras que queremos extraer
resultado = "".join(filter(letras.__contains__,texto))
print(resultado)

#Buscar subcadenas en una cadena de texto
cadena = 'Hola, Mundo'

#Buscamos la posicion de la subcaddena "mundo"
indice = cadena.find('Mundo')
print(f"indice de la subcadena 'Hola':{indice}")