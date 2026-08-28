texto= "la vaca lola, tiene cabeza y tiene cola "
letras= "a"
resultado = "".join(filter(letras.__contains__,texto))
print(resultado)
conteo= len(resultado)
print(conteo)