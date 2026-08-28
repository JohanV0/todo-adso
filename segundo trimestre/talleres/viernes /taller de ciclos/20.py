password = input('Digite su contraseña: ') #se guarda la contraseña 
MAYUSCULAS = 'ABCDEFGHIJKLMNÑOPQRSTWXYZ' #se guardan las mayusculas 
NUMEROS = '1234567890' #se guardan los numeros 

tiene_mayuscula = False #se toma como que no tiene mayusculas
tiene_numero = False #se toma como que no tiene numeros
no_tiene_espacios = True #se toma como que si tiene espacios 

for i in password:#se evalua si la contraseña cumple con las condicionas comparando la contraseña ingresada vs las variables anteriores 
    if i in MAYUSCULAS:
        tiene_mayuscula =  True

    if i in NUMEROS:
        tiene_numero = True

    if i == ' ':
        no_tiene_espacios = False

if tiene_mayuscula == True and tiene_numero == True and no_tiene_espacios == True: #se muestra en caso de que todo sea verdadero
    print('Contraseña segura')

elif tiene_mayuscula == False and tiene_numero == True and no_tiene_espacios == True: #se muestra si tiene todo pero le falta mayuculasa
    print('Constaseña insegura, debe llevar una mayuscula')

elif tiene_mayuscula == False and tiene_numero == False and no_tiene_espacios == True: #se muestra si tiene todo pero le falta numeros
    print('Constaseña insegura, debe llevar una mayuscula y un numero')
    
elif tiene_mayuscula == True and tiene_numero == False and no_tiene_espacios == True: #se muestra si tiene todo pero contiene espacios
    print('Constaseña insegura, debe llevar 1 numero')

else:
    print('La contraseña debe llevar 1 mayuscula, 1 numero y NO debe llevar espacios') #se muestra en caso que no tenga nada correcto