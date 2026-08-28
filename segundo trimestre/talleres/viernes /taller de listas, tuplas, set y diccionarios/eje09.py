texto_nuevo = (
    "Los estudiantes comentan que las actividades son interesantes, pero creen "
    "que sería bueno tener más materiales de apoyo, recibir información con más "
    "claridad y contar con más espacios para resolver dudas."
)

texto_pequeno = texto_nuevo.lower()  # convierte todo el texto a minúsculas

lista_letras = [letra for letra in texto_pequeno if letra.isalpha()]  # guarda solamente las letras y elimina espacios y signos

total = len(lista_letras)  # cuenta cuántas letras hay en total

diccionario = {}
for letra in lista_letras:  # recorre cada letra de la lista y cuenta cuántas veces aparece
    diccionario[letra] = diccionario.get(letra, 0) + 1

diccionario_ordenado = dict(sorted(diccionario.items()))  # ordena las letras de la A a la Z

print(f"Total de letras encontradas: {total}\n")  # muestra el total de letras

print("Frecuencia de cada letra:")
for letra, cantidad in diccionario_ordenado.items():  # muestra cada letra y su cantidad
    print(f" - {letra}: {cantidad}")

if diccionario:  # revisa que el diccionario no esté vacío
    letra_mas = max(diccionario.items(), key=lambda x: x[1])  # busca la letra que más se repite
    letra_menos = min(diccionario.items(), key=lambda x: x[1])  # busca la letra que menos se repite

    print()
    print(f"La letra que más aparece es '{letra_mas[0]}' y salió {letra_mas[1]} veces")
    print(f"La letra que menos aparece es '{letra_menos[0]}' y salió {letra_menos[1]} veces")
else:
    print("No se encontraron letras en el texto.")  # mensaje si no hay letras

letras_repetidas = [(letra, cantidad) for letra, cantidad in diccionario.items() if cantidad > 3]  # guarda las letras que aparecen más de 3 veces

letras_repetidas.sort(key=lambda x: x[1], reverse=True)  # ordena de mayor a menor

print()
print("Letras que aparecen más de 3 veces:")

for letra, cantidad in letras_repetidas:  # recorre las letras encontradas
    porcentaje = (cantidad / total) * 100 if total else 0  # calcula el porcentaje que representa cada letra
    print(f" - {letra}: {cantidad} veces - {porcentaje:.2f}% del total")