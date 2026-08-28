# numeros = [15,3,22,7,9,1]
# mayor = numeros[0]
# menor = numeros[0]
# suma = 0
# for n in numeros:
# 	if n > mayor:
# 		mayor = n
# 	if n < menor:
# 		menor = n
# 	suma += n
# print(f'El numero mayor es: {mayor}, el numero menor es: {menor} y la suma de todos los numeros es: {suma}')

# numeros = [4, 9, 2, 7, 5, 8]
# contador = 0
# suma = 0
# for n in numeros:
#     if n % 2 == 0:
#         contador += 1
#         suma += contador
# print(f'los numeros pares de la lista son: {contador} y la suma de los pares es: {suma}')

# numeros = [10, 3, 6, 1, 8, 2]
# pares= None
# impares = None
# for n in numeros:
#     if n % 2 == 0:
#         if pares is None or n > pares:
#             pares = n
#     else:
#         if impares is None or n < impares:
#             impares = n
# print(f'el numero mayor PAR es: {pares}, el numero menor IMPAR es:{impares}')

# numeros = [5, 10, 15, 20]
# for n in range(len(numeros)):
#     print(numeros[n]*2)
# numeros = [3, 6, 9, 12, 15]
# suma=0

# for i in range(len(numeros)):
#     if i % 2 == 0:
#         suma += numeros[i]
# print(f'la suma de las posiciones pares son: {suma}')
# numeros = [10, 20, 30, 40, 50]
# nueva = []

# for i in range(len(numeros)):
#     if i % 2 == 0:
#         nueva.append(numeros[i])
#     else:
#         nueva.append(numeros[i]*2)
# print(f'{nueva}')

# numeros = [5, 10, 15, 20, 25]
# par_impar=[]
# for i in range(len(numeros)):
#     if i % 2 == 0:
#         par_impar.append(numeros[i]//2)
#     else:
#         par_impar.append(numeros[i]*3)
# print(f'{par_impar}')

# def cuadruple(x):
#     return x * 4
# x= cuadruple(9)
# print(x)

# def mayor (a,b):
#     mayor=0
#     if a>b:
#         return f'{a} es mayor que {b}'
#     else:
#         return f'{b} es mayor que {a}'
# print(mayor(10,3))

# def sumar_lista(lista):
#     suma=0
#     for n in lista:
#         suma += n
#     return suma
# print(sumar_lista([1,2,3,4]))

# def fun1(a):
#     return None
# def fun2(a):
#     return fun1(a)*fun1(a)
# print(fun2(2))

# lts= [[x for x in range(3)]for y in range(3)]
# for r in range (3):
#     for c in range(3):
#         if lts[r][c] % 2!=0:
#             print("#")
# print("a","b","c",sep="sep")

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']
# for k in range(len(dct)):
#     v = dct [v]
# print(v)

# foo=(1,2,3)
# foo.index(0)

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a,b)

# my_list = [x * x for x in range(5)]
# def fun(lst):
#     del lst [lst[2]]
#     return lst
# print(my_list)
# print(fun(my_list))