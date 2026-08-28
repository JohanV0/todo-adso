def generar_usuario(texto):
    lista_texto = texto.lower().split()
    primeral_etra = lista_texto[0]
    apellido = lista_texto[2]
    return primeral_etra[0] + apellido  
def validar_usuario(usuario,lista_usuarios):
    numero = 0
    while usuario in lista_usuarios:
        numero += 1
        nuevo_usuario = usuario + str(numero)
        if nuevo_usuario in lista_usuarios:
            continue
        return nuevo_usuario
    else:
        return False

usuarios = [
    "jvergara",
    "jvergara1",
    "jvergara2",
    "jvergara3",
    "mgomez",
    "cperez",
    "arodriguez",
    "lmartinez",
    "jhernandez",
    "psanchez",
    "rtorres",
    "dgarcia",
    "fvargas",
    "ccastro",
    "abustos",
    "emorales",
    "nsuarez",
    "jramirez",
    "osalazar",
    "qvillamil",
    "iblanco",
    "mmendoza",
    "ahoyos"
]

usuario_generado = generar_usuario(input('Digite su nombre completo. Cada uno separado por coma: '))
validacion = validar_usuario(usuario_generado, usuarios) 
print(f'El usuario generado es: {usuario_generado} ')
print(f'El usuario generado es valido?: {validacion}')