password = input('Digite su contraseña: ')

largo_password = 8
min_mayus = False
num_permitidos = False
NUMEROS = '0','1','2','3','4','5','6','7','8','9'

if len(password) >= largo_password:
    largo_password = True
else:
    largo_password = False

if '0' in password or '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password : 
    num_permitidos = True
else:
    num_permitidos = False

if password.lower() != password:
    min_mayus = True
else:
    min_mayus = False
if largo_password == True and num_permitidos == True and min_mayus == True:
    print(f'contraseña aceptada')
elif largo_password == False and num_permitidos == True and min_mayus == True:
    print(f'la contraseña debe tener minimo 8 caracteres')
elif largo_password == True and num_permitidos == False and min_mayus == True:
    print(f'la cotraseña debe de tener minimo un numero')
elif largo_password == True and num_permitidos == True and min_mayus == False:
    print(f'la contrasela debe tener minimio una mayuscula')
else:
    print(f'la contraseña debe contener minimo 8 caracteres, 1 numero y 1 mayuscula') 