# text = 'cien años de soledad'
# if 'años' in text:
#     print('yes')
# else:
#     print('no')

# cadena = input('digite una frase: ')
# if 'colombia' in cadena:
#     print('yes')
# else:
#     print('no')

# s = "hola amigos mios"
# for letra in s: #se puede iterar cada letra de la cadena
#     print(letra, end = ", ")

# frase_2 = input("digite una frase: ")
# for letra in frase_2: #se puede iterar cada letra de la cadena
#     print(letra, end = ", ")

frase = input('digite el nombre completo del SENA: ').strip().upper()
inicio = 'amor'
final = 'felicidad'
concatenacion = inicio + " " + frase + " " + final

for letras in concatenacion:
    print(f'{letras}', end=", ")

