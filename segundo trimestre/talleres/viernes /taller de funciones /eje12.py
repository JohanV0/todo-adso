def contar_palabras(reseña):
    cantidad_palabras = len(reseña.split())
    return cantidad_palabras

def buscar_palabras_clave(reseña,palabras_claves):

    reseña = reseña.lower()
    for signo in ".,;:!?()\"'":
        reseña = reseña.replace(signo, "")

    palabras  = reseña.split()
    conjunto_palabras = set()

    for n in palabras:
        if n in palabras_claves:
            conjunto_palabras.add(n)
    return conjunto_palabras

def clasificar_reseña(reseña, palabras_positivas, palabras_negativas):
    positivas = buscar_palabras_clave(reseña, palabras_positivas)
    negativas = buscar_palabras_clave(reseña, palabras_negativas)

    if len(positivas) > len(negativas):
        return "Positiva"
    elif len(negativas) > len(positivas):
        return "Negativa"
    else:
        return "Neutra"

palabras_positivas = {
    "excelente",
    "buena",
    "buenas",
    "emocionante",
    "entretenida",
    "interesante",
    "genial",
    "increíble"
}

palabras_negativas = {
    "mala",
    "malas",
    "aburrida",
    "aburridas",
    "lenta",
    "lento",
    "confuso",
    "malo"
}
reseña = input("Ingrese la reseña: ")
print(f"Total de palabras: {contar_palabras(reseña)}")
print(f"Clasificación: {clasificar_reseña(reseña,palabras_positivas,palabras_negativas)}")