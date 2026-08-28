nombre = input('digite su nombre completo: ')
ciudad = input('ingrese la ciudad donde vive: ')
ocupacion = input('¿en que trabaja?: ')
edad = int(input('digte su edad: '))

print('''
\nPerfil del usuario
--------------------
opciones del usuario:
    
Opcion 1
Opcion 2
Opcion 3
Opcion 4
Opcion 5
Opcion 6
Opcion 7
    
Nota: Elegir la opcion por nombre o numero''')

opcion = input('¿Cual es las opciones desea usar?: ').lower().strip()
opciones_validas = '1','2','3','4','5','6','7','opcion 1''opcion ','opcion 3','opcion 4','opcion 5','opcion 6','opcion 7'

if opcion == '1' or 'opcion 1':
    print(f"¡Hola, {nombre}! Bienvenido/a al sistema." )
elif opcion == '2' or 'opcion 2':
    print(f"Actualmente te encuentras en {ciudad}." )
elif opcion == '3' or 'opcion 3':
    print(f"Tu ocupación es: {ocupacion}"  )
elif opcion == '4' or 'opcion 4':
    if edad >= 18:
        print('Usted es mayor de edad')
    else:
        print('Usted es menor de edad')
elif opcion == '5' or 'opcion 5':
    print(f'''
    Resumen de datos:
    Nombre = {nombre}
    Ciudad = {ciudad}
    ocupacion = {ocupacion}
    edad = {edad}
''' )
    
elif opcion == '7' or 'opcion 7':
    cambio_nombre = input(f"¿Cambiar nombre? Digite su nuevo nombre: " )
    print(f'Nombre anterior: {nombre} -> Nombre actual: {cambio_nombre}')

elif opcion == '6' or 'opcion 6':
    print(f"Hasta luego, {nombre}. Sesion cerrada." )

else:
    print('la opcion ingresada no es valida')