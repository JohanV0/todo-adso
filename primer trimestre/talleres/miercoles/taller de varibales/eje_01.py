#1.definir - asignar
nombre = str('johan')
numero = int(1)
numero_decimal = float(22.3)
efectivo = bool(True)

#2.capturar 
str = str(input('digite su nombre: '))
int = int(input('digite un numero entero al azar: '))
float = float(input('digite un numero decimal con (.): '))
bool = bool(input('Tiene efectivo?: '))

str_2 = type(str)
int_2 = type(int)
float_2 = type(float)
efectivo = bool == 'si'
bool_2 = type(bool)

#3. mostrar
print(f'''
    su nombre es: {str} y el tipo es: {str_2}
    el numero ingresado entero es: {int} y el tipo es: {int_2}
    el numero ingresado decimal es: {float} y el tipo es: {float_2}
    ¿el numero ingresado es entero?: {bool} y el tipo es: {bool_2}''')
