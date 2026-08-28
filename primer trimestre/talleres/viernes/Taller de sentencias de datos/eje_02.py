rol = input('ingrese su rol (admin/supervisor): ').strip().lower().title() == "Admin" or "Supervisor"
password = input('ingrese su contraseña: ').strip().lower().title()

if rol == True and len(password) >= 5:
    print('contraseña cumple con las condiciones')
elif rol == True and len(password) < 5:
    print('contraseña con caracteres insuficientes')
elif rol == False and len(password) >= 6:
    print('rol incorrecto')
elif rol == False and len(password) < 5:
    print('rol incorrecto y contraseña incorrectos')
else:
    print('valores vacios')