#variables necesarias
salir = False
contador_busqueda = 0
contador_novedades = 0

while not salir:#MIentra no sea verdadero siga y muestre el print
    print(''' Sistema de Biblioteca
1.Buscar libro
2.Novedades
3.Salir
''')
    opcion = int(input('Elija la opcion que quiere usar: (1 / 2 / 3): '))#Se guarda la opcon en la variable opcion
    if opcion == 1:#Si es 1 Se muestra el print de busqueda y se aumenta el busccador de las veces buscadas
        contador_busqueda += 1
        print('Realizando busqueda... Listo. Porfavor: \n')
    elif opcion == 2:#Si es 2 Se muestra el print de busqueda y se aumenta el busccador de las veces buscadas novedades
        contador_novedades += 1
        print('Realizando busqueda de novedades... Listo. Porfavor: \n')
    elif opcion == 3:#Si es 3 se muestra las veces del contador de cada una 
        salir = True
        print(f'Conteo de busquedas: {contador_busqueda}. Conteo de novedades: {contador_novedades}')
    else:
        print('Advertencia, la opcion ingresada no es valida. \n')#Si no es una opcion valida se muestra el mensaje y se repite la variable opcion
else:
    print('Saliendo del programa.... Adios.')