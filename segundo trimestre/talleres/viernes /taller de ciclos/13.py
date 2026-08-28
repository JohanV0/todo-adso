salir = False # Indica que no va a salir
palabra_error = 'error' # Palabra que se va a contar como error
palabra_correcto = 'correcto' # Palabra que se va a contar como correcto
errores = 0 # Contador de errores empieza en 0 porque no ha comenzado
correcto = 0 # Contador de correctos empieza en 0 porque no ha comenzado

while not salir: # Mientras la variable sea falsa no salga
    frase = input('Ingrese la frase (si desea salir digite salir): ').lower() # Ingresa la frase del usuario y la convierte a minusculas

    if frase == 'salir': # Si el usuario digita salir termina el ciclo
        salir = True # Cambia la variable a verdadero para salir
    else:
        palabra_actual = "" # Se guarda la palabra que se va armando letra por letra

        for i in range(len(frase)): # Recorre la frase letra por letra
            letra = frase[i] # Se obtiene la letra en la posicion actual

            # Si la letra no es espacio ni puntuacion la agrega a la palabra actual
            if letra != " " and letra != "," and letra != "." and letra != ";" and letra != ":":
                palabra_actual += letra # Se va armando la palabra letra por letra
            else:
                if palabra_actual == palabra_error: # Si la palabra armada es error suma 1
                    errores += 1 # Se aumenta el contador de errores
                if palabra_actual == palabra_correcto: # Si la palabra armada es correcto suma 1
                    correcto += 1 # Se aumenta el contador de correctos
                palabra_actual = "" # Se reinicia la palabra para armar la siguiente

        # Se verifica la ultima palabra porque no tiene espacio ni puntuacion al final
        if palabra_actual == palabra_error: # Si la ultima palabra es error suma 1
            errores += 1 # Se aumenta el contador de errores
        if palabra_actual == palabra_correcto: # Si la ultima palabra es correcto suma 1
            correcto += 1 # Se aumenta el contador de correctos

        print("Errores encontrados:", errores) # Muestra cuantos errores se encontraron
        print("Correctos encontrados:", correcto) # Muestra cuantos correctos se encontraron

print('Saliendo del sistema.... Adios.') # Mensaje de despedida cuando el usuario decide salir