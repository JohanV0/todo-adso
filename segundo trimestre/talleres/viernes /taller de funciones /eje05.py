def contar_vocales(nombre_producto):
        solo_vocales = []
        dic_vocales = {}
        for n in nombre_producto:
            if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':  
                solo_vocales.append(n)
        for j in solo_vocales:
             dic_vocales[j] = dic_vocales.get (j, 0) + 1
        return dic_vocales
frase = 'ola mundo'
print(contar_vocales(frase))