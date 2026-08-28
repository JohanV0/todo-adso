nombre_completo = input('El Guardián del Templo pide el nombre completo del aprendiz: ')
nombre_numeros = '0','1','2','3','4','5','6','7','8','9'
if  nombre_completo != nombre_numeros:
    nombre_mayuscula = nombre_completo.upper()
    nombre_contrario = nombre_completo[::-1]
    nombre_palindormo = nombre_contrario == nombre_completo
    nombre_vocales = nombre_completo.upper().count("A") + nombre_completo.count("E") + nombre_completo.count("I") + nombre_completo.count("O") + nombre_completo.count("U")
    nombre_cambio_a = nombre_completo.replace('A','*') + nombre_completo.replace('E','*') +nombre_completo.replace('I','*') +nombre_completo.replace('O','*') +nombre_completo.replace('U','*')+nombre_completo.replace('a','*') +nombre_completo.replace('e','*') +nombre_completo.replace('i','*') +nombre_completo.replace('o','*') +nombre_completo.replace('u','*') 
    nombre_largo = len(nombre_completo.replace(' ',''))

    print(f'''
    nombre en mayusculas: {nombre_mayuscula}
    nombre al reve: {nombre_contrario}
    ¿nombre palindromo?: {nombre_palindormo}
    numero de volcales del nombre: {nombre_vocales}
    ''')
    pregunta_guardian = input("Cuantas letras tiene tu nombre (sin espacios)?: ")
    if pregunta_guardian == nombre_largo:
        print("Sabiduria confirmada. Puedes pasar." )
    else:
        print("Tu mente aun no conoce tu propio nombre." )

else:
    print('El guardian rechaza al aprendiz por llevar un numero')
