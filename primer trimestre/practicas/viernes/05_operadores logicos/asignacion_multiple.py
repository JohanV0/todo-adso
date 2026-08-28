# asignacion multiple cadena
#operacionde asignacion es (=)
numero=5
numero=10

# asignacion multiple
x, y, z= 5,'Hola',-9.15

print(f'Valor de x = {x}, valor de y = {y}, valor de z = {z}')

#asignacion en cadena

a = b = c = 10
print(f'Valor de a = {a}, valor de b = {b}, valor de c = {c}')

#intercambio de valores sin variables temporales

x, y = 5, 10
print(f'Valores iniciales: x = {x}, y = {y}') #valores iniciales

#aplicando el concepto de asignacion multiple para intercambiar valores 
x, y = y, x
print(f'invertir valores x = {x}, y = {y}')

nombre,apellido=input("ingrese su nombre y apellido separado por coma: ").split(',')
#.split sirve para dividir la cadena en una lista, en este casi con la ","
print(f'Nombre: {nombre.strip().lower().replace(" ","")}, Apellido: {apellido.strip().lower().replace(" ","")}')
