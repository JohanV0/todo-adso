


parrafo = (
    "Durante la reunión semanal del equipo de desarrollo, se discutieron nuevas "
    "estrategias para optimizar el rendimiento de la aplicación, mejorar la "
    "experiencia de usuario y reforzar la seguridad de los datos; además se "
    "propusieron capacitaciones internas sobre tecnologías emergentes."
)


limpiar = parrafo.lower()#se convierte el texto a minusculas 
for ch in ['.', ',', ';', ':', '!', '?', '¿', '¡']: #con una lista se comprara el texto y se sacan los que estan con replace por un espacio vacio
    limpiar = limpiar.replace(ch, '')

palabras = limpiar.split() #convierte el texto en una lista que separa las palabras

total_palabras = len(palabras) #con len se saca las palabras de la lista palabras 

palabras_unicas = sorted(set(palabras)) #sorted organiza las palabras alfabeticamente y set hace que no se pueda modificar 

#se imprime todo
print(f"Total de palabras: {total_palabras}")
print(f"Todas las palabras únicas: {len(palabras_unicas)}")

frecuencias = {}#se crea un diccionario vacio que se va a llenar con un ciclo for (diccionario de frecuencias), si la palabra ya esta, se suma al contador, sino se crea una con el contador 1
for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1

print("Aparicion de palabras (alfabeticamente): ")
for w,j in sorted(frecuencias.items()): #para w y j en el diccionario frecuencias se ordena de manera alfabetica y se imprime w que es el key y c que es el value
    print(f" - {w}: {j}")
print()

# Identificar las 5 palabras que más se repiten
top5 = dict(sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:5]) #se guarda en una variable que coje los parametros del diccionario frecuencia y con la funcion lamba lo ordena de manera alfabetica usando reverse en la posicion del valor y solo muestra los valores primero usando [:5] por ultimo, todo lo convierte en diccionario
print("Top 5 palabras más repetidas: ")#se muestra en la pantalla
for w, c in top5.items(): #para w y c en el diccionario se imprimer el key y el valor de manera iterada por un for 
    print(f" - {w}: {c}")
print()

excluidas = {'el', 'la', 'de', 'y', 'en', 'a', 'que', 'es', 'los', 'las', 'un', 'una', 'se', 'con', 'del', 'por'}

# Reconstruir frecuencias con las palabras excluidas
frecuencias_filtradas = {}#se crea un diccionario donde se va a guardar
for p in palabras:# para p en palabras, si p esta en el diccionario excluidas ignore, si p ya estaba en la lista de frecuencias_flitradas se suma una, sino se crea un nuevo valor con el contador de 1
    if p in excluidas:
        continue
    if p in frecuencias_filtradas:
        frecuencias_filtradas[p] += 1
    else:
        frecuencias_filtradas[p] = 1

top5_filtrado = dict (sorted(frecuencias_filtradas.items(), key=lambda x: x[1], reverse=True)[:5]) #se guarda en top5_filtrado elf diccionario frecuencias_filtradas ordenado por sorted de manera alfabetica, con items y la funcion lambda se organiza segun el value y se muestra solo los 5 primeros con [:5]
print("Top 5 palabras más repetidas (sin stopwords):")
for w, c in top5_filtrado.items():#para w y c en el diccionario top5_filtrado se imprime el key con el value de manera iterada 
    print(f" - {w}: {c}")
