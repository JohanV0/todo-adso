#operadores aritmetios en python

#fedinimos dos variables

a=10
b=3

#suma(+)
suma= a+b
print(f'suma: {suma}')

#resta(-)
resta= a-b
print(f'Resta: {resta}')

#multiplicacion(*)
multi= a*b
print(f'Multiplicacion: {multi}')

#division float(/)
div_float=a/b #se divide 'a' entre b''(10 / 3 = 3.3333...)
print(f'Division: {div_float:.2f}') #se imprime el resultado con dos decimales 

#divisionn entera(//)
div_int=a//b
print(f'Division entera {div_int}')

#modulo(%) saca el residuo de la division
div_residuo=a%b
print(f'Division con residuo: {div_residuo}')

#exponente(**) eleva a la potencia despues del **
exponente=a**b #10 elevado a la 3 (10^3) es 10*10*10 = 1000
print(f'Exponente: {exponente}')

