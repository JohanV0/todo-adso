frase=input('ingrese su nombre: ')
letras = "error"
resultado = "".join(filter(letras.__contains__,frase))
conteo=len(resultado)
print(resultado)
if resultado != 'error':
    resultado ='error'
    print(resultado)