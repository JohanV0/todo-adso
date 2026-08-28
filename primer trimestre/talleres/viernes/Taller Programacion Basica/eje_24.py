USUARIO='johan_01'
PASSWORD='hola mundo'

usuario=input('ingrese su usuario registrado: ')
password=input('ingrese su contraseña registrada: ')

usuario = usuario == USUARIO
password = password == PASSWORD

print(f'''
      El usuario es: {usuario}
      La contraseña es: {password}''')