def tiene_arroba_unica(correo):
    contador = 0
    for letra in correo:
        if letra == "@":
            contador += 1
    return contador == 1

def separar_correo(correo):
    return correo.split("@")

def dominio_permitido(dominio, dominios):
    return dominio in dominios

def validar_correo_completo(correo, dominios):
    if not tiene_arroba_unica(correo):
        return "Correo inválido: debe tener una sola @"
    usuario, dominio = separar_correo(correo)
    if usuario == "":
        return "Correo inválido: usuario vacío"
    if " " in usuario:
        return "Correo inválido: el usuario tiene espacios"
    if not dominio_permitido(dominio, dominios):
        return "Correo inválido: dominio no permitido"
    return "Correo válido"

dominios = {
    "gmail.com",
    "hotmail.com",
    "outlook.com",
    "misena.edu.co"
}

for i in range(5):
    correo = input(f"Correo {i+1}: ")
    print(validar_correo_completo(correo, dominios))