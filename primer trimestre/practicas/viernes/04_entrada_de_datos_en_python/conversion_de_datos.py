#conversion de tipos de datos
#-------------------------------------------------------------------
#conversion de cadena a numero entero

numero_cadena= '10'

#se convierte la cadena a un numero entero con la funcion int()

numero_entero=int(numero_cadena)
print(f'\n Valor numero en cadena: {numero_cadena}, y el tipo de dato es: ', type(numero_cadena))
print(f'Cadena a entero: : {numero_entero}, y el tipo de dato es: ', type(numero_entero))

#conversion de cadena a numero decimal (float)
print('-------------------------------------------------------------------')
numero_cadena='3.14'
numero_float=float(numero_cadena)
print(f'\n Valor numero en cadena: {numero_cadena}, y el tipo de dato es: ', type(numero_cadena))
print(f'Cadena a float: : {numero_float}, y el tipo de dato es: ', type(numero_float))

#conversion de numero entero a cadena
print('-------------------------------------------------------------------')
numero_entero='30'
numero_cadena=str(numero_entero)
print(f'\n Valor numero en entero: {numero_entero}, y el tipo de dato es: ', type(numero_entero))
print(f'Entero a cadena: : {numero_cadena}, y el tipo de dato es: ', type(numero_cadena))

#conversion de booleano(bool)
print('-------------------------------------------------------------------')
#en python ciertos valores son considerados false
#ejemplo con el cero
numero_entero = 0
booleano = bool(numero_entero)
print(f'\n Valor booleano de cero: {booleano}, y el tipo de dato es: ',type(booleano))

#ejemplo con numero dstinto a cero
print('-------------------------------------------------------------------')
numero_entero = 5
booleano = bool(numero_entero)
print(f'\n Valor booleano diferente de cero: {booleano}, y el tipo de dato es: ',type(booleano))

print('-------------------------------------------------------------------')
#ejemplo con cadena vacia
numero_entero = ''
booleano = bool(numero_entero)
print(f'\n Valor booleano de cadena vacia: {booleano}, y el tipo de dato es: ',type(booleano))

print('-------------------------------------------------------------------')
#ejemplo con cadena llena
numero_entero = 'cadena con valor'
booleano = bool(numero_entero)
print(f'\n Valor booleano de cadena con valor: {booleano}, y el tipo de dato es: ',type(booleano))

print('-------------------------------------------------------------------')
#ejemplo con None (valor nulo en python)
numero_entero = None
booleano = bool(numero_entero)
print(f'\n Valor booleano de None: {booleano}, y el tipo de dato es: ',type(booleano))