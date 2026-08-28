#Todas las variables constates necesarias 
acumulador = 0 
acumulador_temperatura = 0
limite_temperatura = -999
temperatura_alta = 0
temperatura_baja = 0
temperatura_media = 0
while not False: #Mientras no sea falso, siga:
    temperatura = int(input('Digite la temperatura de ambiental (en numeros enteros): '))#Ingresar la temperatura
    acumulador += 1 #Se aumenta el acumulador cada vez que se ingresa una temperatura
    if temperatura > 30:#Si la temperatura es mayor a 30 aumente el contador de temperatura alta y guarde la temperatura
         temperatura_alta += 1
         acumulador_temperatura += temperatura 
    elif temperatura >= 15 and temperatura <=30:#Si la temperatura esta entre 15 y 30 aumente el contador de temperatura media y guarde la temperatura
         temperatura_media +=1
         acumulador_temperatura += temperatura 
    elif temperatura < 15:#Si la temperatura es menor a 15 aumente el contador de temperatura baja y guarde la temperatura
         temperatura_baja +=1
         acumulador_temperatura += temperatura 
    salida = input(f'Si desea salir digite "-999", si desea continuar digite "continuar": ') #Si desea continuar o terminar
    if salida == '-999':#Se termina cuando digite -999 y muestra el print
        prom_temperatura = acumulador_temperatura / acumulador
        print(f'''
            Cantidades del ambiente registradas: {acumulador}
            Temperaturas altas: {temperatura_alta}
            Temperaturas media: {temperatura_media}
            Temperaturas baja: {temperatura_baja}
            promedio de temperaturas: {prom_temperatura}
''')
    elif salida == 'continuar':#Si digita continuar se repite
          continue
    else:
          print('digite un valor valido, Se continua por defecto\n')#Si no de digita salir o continuar se contninua el codigo por defecto
else:
      print('se termino el registro de participantes')
