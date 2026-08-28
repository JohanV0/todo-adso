def validar_longitud(texto):
    validacion = False
    if len(texto) >=6 and len(texto)<=10:
        validacion = True
    else:
        validacion = False
    return validacion
def validas_solo_digitos(valida_longitud):
    validacion = False
    contenedor_variable = ''
    for n in str(valida_longitud):
        if n.isdigit() == True:
            validacion = True
            contenedor_variable += n
        else:
            validacion = False
            break
    return validacion
def validar_no_repetidos(list,usuario):
    duplicado = False
    if usuario in list:
        duplicado = True
    else:
        duplicado = False
    return duplicado

def validar_identificacion(longitud,digitos,duplicado):
    if longitud and digitos and duplicado is True:
        validacion = True
    else:
        validacion = False
    return validacion

numeros = [
    "123456",
    "9876543",
    "45678901",
    "765432109",
    "11111111",
    "2222222222",
    "333333333",
    "44444444"
]
identificacion = input('Digite la identificacion: ')
longitud = (validar_longitud(identificacion))
digitos = (validas_solo_digitos(identificacion))
duplicado = (validar_no_repetidos(numeros,identificacion))
comprobacion = validar_identificacion(longitud,digitos,duplicado)
print(f'''
Comprobacion: 
- Longitud is correct? : {longitud}
- Digit is correct? : {digitos}
- Duplicate is correct? : {duplicado}
- Comprobacion : {comprobacion}
''')
