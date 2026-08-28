acumulador = 0 #Acumulador empieza en 0
salir = False #Indica que no va a salir 
contador_caracteres = 0 #contador de los caracteres empieza en 0 porque no a comenzado

while not False: #mientras la variable sea falsa no salga
    nombre = input('Usuario porfavor digite su nombre completo: ').strip() #Ingresa el nombre del usuario
    acumulador += 1 #Se aumenta el acumulador de usuarios las veces que se ingrese
    salida = input(f'Si desea salir digite "fin", si desea continuar digite "continuar": ') #Si desea salir o continuar
    if salida == 'fin': #Si se sale muestra el acumulador de usuarios y los que estan arriba de 5 caracteres en el nombre
            nombre_mayor_5 = len(nombre)
            if nombre_mayor_5 > 5 and salida == 'fin':
                contador_caracteres += 1
                print(f'Cantidad de nombres regisrados: {acumulador}, los mayores a 5 caracteres son: {contador_caracteres}')
                break
    elif salida == 'continuar': #Se repite lo de ingresar el nombre
          continue
    else:
          print('digite un valor valido') #Si se ingresa un valor que no sea caracter
else:
      print('se termino el registro de participantes')
