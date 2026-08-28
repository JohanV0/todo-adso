# # #Entrada de datos(string-cadena-caracteres)

# # nombre=(input("ingrese el nombre: "))
# # print("Su nombre es: ",nombre)

# # nombre_padre=(input("ingrese el nombre de su padre: "))
# # print("El nombre de su padre es: ",nombre_padre)

# # nombre_madre=(input("ingrese el nombre de su madre: "))
# # print("El nombre de su madre es: ",nombre_madre)

# # #entrada de de datos(Numeros-entero)

# # Numero=input("\n 1.ingrese un numero: ")
# # print("el numero es: ",Numero)

# # #Numero=input("\ningrese un numero: ")
# # #print("el numero es: ",Numero + 4) error porque numero esta definido como caracter

# # #convertir de texto a numero forma 1:
# # Numero=input("\n 2.ingrese un numero: ")
# # Numero=int(Numero)
# # print("el numero es: ",Numero + 4) 

# # #convertir de texto a numero forma 2:
# # Numero=int(input("\n 3.ingrese un numero: "))
# # print("el numero es: ",Numero + 4)

# # #numero float
# # numero=float(input("Ingrese un numero: "))
# # print("el numero es: ",numero+3.5)

# #numero= input("ingrese el numero: ")
# #print(numero)

# #numero=input("ingrese el numero: ")
# #print(type(numero))

print("perimetro del circulo")
radio=float(input("digite el radio de circulo: "))
pi=3.1416
perimetro=2*pi*radio
print("el perimetro del circulo es: ", perimetro)
print("---------------------------------------------------------------")

print("\narea del circulo")
area_circulo=pi*radio**2
print("el area del circulo es de: ",area_circulo)
print("---------------------------------------------------------------")

print("area del cuadrado")
lado=float(input("digite el lado del cuadrado: "))
area=lado**2
print(f'el area del cuadrado es: {area}')
print("---------------------------------------------------------------")

print("perimetro del cuadrado")
lado2=float(input("digite el lado del cuadrado: "))
perimetro_cuadrado=lado2**3
print(f'el perimetro del cuadrado es: {perimetro_cuadrado}')

print("PROMEDIO DE NOTAS")
nom=input("ingrese su nombre: ")
nota1=float(input("digite su primera nota: "))
nota2=float(input("digite su segunda nota: "))
nota3=float(input("digite su tercera nota: "))
nota4=float(input("digite su cuarta nota: "))

sum=nota1+nota2+nota3+nota4
prom=sum/4
print(f"el promedio de su nota es: {prom}")