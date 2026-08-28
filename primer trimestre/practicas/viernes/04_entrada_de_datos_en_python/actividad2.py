
from random import randint
nombre=(input("digite su nombre del producto: "))
categoria=(input("digite categoria del producto: "))
año=int(input("digite año de fabricacion: "))
num=randint(100,999)

nombre=nombre.strip().replace(" ","")

subnombre = nombre.upper().strip().replace(" ","")
sub_nombre = subnombre[0:3]
subcategoria= categoria.upper().strip().replace(" ","")
sub_categoria = subcategoria[0:2]
año_str=str(año).strip().replace(" ","")
sub_año=año_str[2:4]

print(f'Su identificaion de {sub_nombre} es de:{sub_nombre}{sub_categoria}{sub_año}{num}')