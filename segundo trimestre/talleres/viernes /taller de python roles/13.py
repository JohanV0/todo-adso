primera_palabra = input('Ingrese la primera palabra: ').strip()
segunda_palabra = input('la segunda palabra: ').strip()


if primera_palabra == "" or segunda_palabra == "":
    print('Error palabras vacias')
else:
    palindromo_1 = primera_palabra[::-1]
    palindromo_2 = segunda_palabra[::-1]
    anagrama_palabra1,palabra1_minuscula,isograma_palabra1,longitud_palabra1 = primera_palabra.lower().strip()
    anagrama_palabra2,palabra2_minuscula,isograma_palabra2,longitud_palabra2 = segunda_palabra.lower().strip()
    anagrama = sorted(anagrama_palabra1) == sorted(anagrama_palabra2) and anagrama_palabra1 != anagrama_palabra2
    iguales = palabra1_minuscula == palabra2_minuscula
    isograma_palabra1 = len(isograma_palabra1) == len(set(isograma_palabra1))
    isograma_palabra2 = len(isograma_palabra2) == len(set(isograma_palabra2))
    longitud_palabra1 = longitud_palabra1.replace(" ","")
    longitud_palabra1 = len(longitud_palabra1)
    longitud_palabra2 = longitud_palabra2.replace(" ","")
    longitud_palabra2 = len(longitud_palabra2)
    print(f'''
La primera palabra es Palindromo?: {palindromo_1}
La segunda palabra es Palindromo?: {palindromo_1}
La Primera palabra es anagrama?: {anagrama_palabra1}
La Segunda palabra es anagrama?: {anagrama_palabra2}
Las Palabras son iguales?: {iguales}
Longitud de la Primera palabra: {longitud_palabra1}
Longitud de la Segunda palabra: {longitud_palabra2}
La Primera palabra es isograma? {isograma_palabra1}
La Primera segunda es isograma? {isograma_palabra2}
''')