palabra = input('digite la palabra en español: ').lower().replace(" ","") #Ingresa la palabra a analizar en español
vocales = 'a','e','i','o','u' #Saca las que NO son consonantes
consonantes = len(palabra) #Se toma todo los caracteres como consonantes
palabra_aprobada = False #Se supone que la palabra no es correcta

if palabra.upper() == palabra and palabra.replace(' ','') == palabra:
    palabra_aprobada = False #SI se cumple el if, se comprueba que la palabra no cumple las condiciones
else:
    palabra_aprobada = True #SI no se sumple, entonces la palabra si cumple con las condiciones
if  palabra_aprobada == True:# si la palabra cumple con condiciones se empieza el if
    for conteo in palabra: # Para cada caracter si es vocal, se le quita un caracter a la palabra que se consideraba como todo consonante
        if conteo  == 'a' in vocales or conteo  == 'e' in vocales or conteo  == 'i' in vocales or conteo  == 'o' in vocales or conteo  == 'u' in vocales:
            consonantes -= 1
            porcentaje_consonantes = (consonantes/len(palabra))*100 #Se saca el porcentaje de consonantes de toda la palabra
        else: #Si no a terminado con las posiciones continue
            continue
#mostramos todo
    print(f''' 
Cantidad de consonantes: {consonantes}
Porcentaje de consonantes: {porcentaje_consonantes:.1f}%''')

