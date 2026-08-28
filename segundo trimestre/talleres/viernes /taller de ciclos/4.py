salida = input('Bienvenido al generador de codigos, si no desea seguir indique "salir", si desea continuar indique "s".')#Se confirma si quiere entrar al codigo, continuar o terminar
codigo = input('ingrese su codigo: ')#Se guarda el codigo en la variable de codigo
#Variables necesarias: 
productos = 0
no_permitido  = 'ERR'
incorrectos = 0

while salida != 'salir':#Mientras no sea verdadero siga:
    if no_permitido not in codigo: #Si esta ERR en el codigo de aumenta el contador de incorrectos productos y se saca el porcentaje 
        incorrectos += 1
        productos += 1
        porcentaje = (productos + incorrectos)*100
        print(f'El codigo indicado es correcto')
        producto = input('Si desea ingresar otro producto escriba "s", si desea salir, escriba "fin": ')
        if producto == 'fin':
            print(f'El porcentaje de productos defectuosos es: {porcentaje}')
            break
        elif producto == 's':
            codigo = input('ingrese su codigo: ').lower().strip()
        else:
            productos -= 1
            print('Solo vale "s" para continuar y "fin" para terminar')
    elif no_permitido in codigo: 
        print(f'El codgio no deve llevar "ERR". Total de productos defectuosos: {incorrectos}')
        reintento = input('Si desea salir esccriba "fin", si desea continuar escriba "s": ').lower().strip()
        if reintento == 'fin':
            break
        elif reintento == 's':
            codigo = input('ingrese su codigo: ')
    else:
        porcentaje = (productos / incorrectos) *100
        print(f'El codigo indicado es correcto')
        producto = input('Si desea ingresar otro producto escriba "s", si desea salir, escriba "fin": ')
        print(f'El porcentaje de productos defectuosos es: {porcentaje}')
else:
    print('se termino el programa de codigo.')