frase = input('Digite su frase o texto: ') #se ingresa la frase 

for i in frase: #se reemplaza la  letra de la izquierda por la de la derecha en caso de encontrarse en la frase 
    if i == 'a':
        frase = frase.replace('a','b')
    elif i == 'm':
        frase = frase.replace('m','n')
    elif i == 'z':
        frase = frase.replace('z','a')
    else:
        continue
    if i == 0: #se reemplaxa el numero de la izquierda por el de la derecha en caso de encontrarse en la frase 
        frase = frase.replace(0,1)
    elif i == 1:
        frase = frase.replace(1,2)
    elif i == 2:
        frase = frase.replace(2,3)
    elif i == 3:
        frase = frase.replace3(3,4)
    elif i == 4:
        frase = frase.replace(4,5)
    elif i == 5:
        frase = frase.replace(5,6)
    elif i == 6:
        frase = frase.replace(6,7)
    elif i == 7:
        frase = frase.replace(7,8)
    elif i == 8:
        frase = frase.replace(8,9)
    elif i == 9:
        frase = frase.replace(9,0)
    else:
        continue
print(f'''La frade codificada es: {frase}
''')