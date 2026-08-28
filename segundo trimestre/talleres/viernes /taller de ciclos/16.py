print('\nCLASIFICACIÓN DE PALABRAS POR LONGUITUD')
print('\nVamos a ingresar los nombres de los estudiantes: ')
#Variables necesarias 
salir= False
nombres_cortos= 0
nombres_largos= 0
nombre_mayor_longitud = 0
nombre_menor_longitud= 0


while not salir:#Mientras no sea verdadero siga
    nombre = input('Ingresa el nombre del estudiante (Para salir digite la palabra "fin"): ')#Se ingresa el nombre de la variable 
    nombre_guardado = nombre#Se guarda el nombre ingresado 

    if len(nombre) > 5:#Si el nombre tiene mas de 5 caracteres siga y se auemnta el contador de nombres largos 
        
        nombres_largos +=1
        if len(nombre) > len(nombre_guardado):
            nombre_mayor_longitud = nombre

        elif len(nombre) < len(nombre_guardado):
            nombre_mayor_longitud = nombre_guardado

        else:

            nombre_mayor_longitud = nombre_guardado and nombre

    
    elif len(nombre) <= 5:
        nombres_cortos += 1
        
        if len(nombre) > len(nombre_guardado):
            nombre_mayor_longitud = nombre
            
        elif len(nombre) < len(nombre_guardado):
            nombre_menor_longitud = nombre_guardado

        else:
            nombre_menor_longitud = nombre_guardado and nombre

    if nombre == 'fin':
        salir= True
        print(f'''CATEGORIA:
              
Cantidad de nombres largos: {nombres_largos} ')
Cantidad de nombres cortos: {nombres_cortos} 
''')

        if len(nombre_mayor_longitud) > 0 and len(nombre_menor_longitud) > 0:
            print(f'''
El nombre mas largo tiene: {len(nombre_mayor_longitud)} caracteres 
El nombre mas corto tiene: {len(nombre_menor_longitud)} caracteres''')