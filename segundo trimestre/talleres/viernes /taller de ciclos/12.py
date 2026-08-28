salir = False
while not False:#Mientras no sea verdadero siga
    palabra = input('Ingrese palabra para comprobar: ').lower()#se guarda la palabra que se quiere saber en la variable palabra 
    if palabra[::-1] == palabra:#Esto invierte el str de la variable palabra y si es verdad se muestra que si es una aplabra capiúa
        print(f'La palabra {palabra} es capicúa. ')
        continuacion = input('Si quiere salir, escriba "salir", si desea seguir presione enter: ')#Se muestra por si quiere sguir en el sistema o quiere salir 
        if continuacion == 'si':#Si digita "si" en la variable continuacion se termina
            salir = True
            print('Adios')
        else:
            continue
    else:
        print(f'La palabra {palabra} no es capiúa')#Se muestra si no es capiúa 
        continuacion = input('Si quiere salir, escriba "salir", si desea seguir presione enter: ')#Se muestra por si quiere sguir en el sistema o quiere salir 
else:
    print('Saliste del sistema. ')