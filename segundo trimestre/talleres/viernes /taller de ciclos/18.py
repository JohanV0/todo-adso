#Variables necesarias donde estan las vocales 
conteo_a = 0
conteo_e = 0
conteo_i = 0
conteo_o = 0
conteo_u = 0
frase = input('Digite su frase o texto: ')#Se guarda la frase en la variable 
for i in frase:#Se compara la posicion de la frase con la letra si esta. Si se cumple se aumenta el contador de la vocal 
    if i == 'a' or i == 'A':
        conteo_a += 1
    elif i == 'e' or i == 'E':
        conteo_e += 1
    elif i == 'i' or i == 'I':
        conteo_i += 1
    elif i == 'o' or i == 'O':
        conteo_o += 1
    elif i == 'u' or i == 'U':
        conteo_u += 1
print(f'''En la frase que ingreso hay:
Total de a: {conteo_a}
Total de e: {conteo_e}
Total de i: {conteo_i}
Total de o: {conteo_o}
Total de u: {conteo_u}
''')#Se muestran los valores sacados de cada uno