print("***playlLst de Canciones***")

#se crea una lista vacía que almacenara

lista_reproduccion=[]

#Solicitamos al usuario que ingrese cuantas canciones desea agregar numero_canciones= int(input ("¿Cuantas canciones desea agregar?"))

numero_canciones = int(input("¿Cuantas canciones desea agregar?: "))
#se utiliza un buble for para repetir tantas veces como canciones indico el usuario

for indice in range (numero_canciones):
    cancion= input (f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

lista_reproduccion.sort()

print ("\nIteramos la playlist")

#Se recorre la lista ordenada

for cancion in lista_reproduccion:
    print(f'- {cancion}')