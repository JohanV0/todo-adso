frase_acceso = input('Digite su frase de acceso: ').strip()

largo = 10
contener = 'dragon'
num_permitidos = False
prohibido = 'prohibido'

if frase_acceso.lower() == prohibido:
    print('la frase no puede llevar la palabra "prohibido". ')
else:
    prohibido == False

if frase_acceso.lower() != frase_acceso + contener:
    contener = True
    print(f'Contener ({contener}). Aprobado')
else:
    contener = False
    print(f'Contener ({contener}). NO Aprobado')
    
if len(frase_acceso) >= largo:
    largo = True
    print(f'Largo de cadena ({largo}). Aprobado')
else:
    largo = False
    print(f'Largo de cadena ({largo}). NO Aprobado')

if '0' in frase_acceso or '1' in frase_acceso or '2' in frase_acceso or '3' in frase_acceso or '4' in frase_acceso or '5' in frase_acceso or '6' in frase_acceso or '7' in frase_acceso or '8' in frase_acceso or '9' in frase_acceso : 
    num_permitidos = True
    print(f'Minimo un numero ({num_permitidos}). Aprobado')
else:
    num_permitidos = False
    print(f'Minimo un numero ({num_permitidos}). NO Aprobado')

if largo == True and num_permitidos == True and contener == True and prohibido == True:
    print(f'frase aceptada. Seguridad 4/4')
elif largo == False and num_permitidos == True and contener == True and prohibido == True:
    print(f'la frase debe tener minimo 10 caracteres. Seguridad 3/4')
elif largo == True and num_permitidos == False and contener == True and prohibido == True:
    print(f'la cotraseña debe de tener minimo un numero de 0 a 9. Seguridad 2/4')
elif largo == True and num_permitidos == True and contener == False and prohibido == True:
    print(f'la contrasela debe tener minimio la palabra "dragon". Seguridad 1/4')
elif largo == True and num_permitidos == True and contener == True and prohibido == False:
    print(f'la contrasela NO debe tener la palabra "prohibido". Seguridad 1/4')
else:
    print(f'la frase debe contener minimo 10 caracteres, 1 numero, la palabra "dragon" y NO debe llevar la palabra prohibido') 