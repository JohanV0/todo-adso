# Variables en python

#Declaracionn e inicializacion de variables
edad = 25 # variables de tipo entero (int)
altura = 1.65 #variable de tipo flotanate (float)
pais = "colombia" #variable de tipo de cadena de texto (str)
vista_al_mar = True #variable de tipo booleano (bool)

#Acceder y mostrar el valor de las variables en la consola
print("Valores iniciales infomacion del usuario:")
print("Edad:", edad)
print("Altura:", altura)
print("Pais:", pais)
print("Vista al mar?:", vista_al_mar)

# modificar el valor de las variables 
edad = 30 # se actualiza el valor de las variables edad
altura = 1.70 # se actualiza el valor de las variables altura
pais = "Francia" 
vista_al_mar = False

print("\nvalor de los datos actualizados" )
print ("Edad:",edad)
print("Altura:",altura)
print("Pais:", pais)
print("Vista al mar?", vista_al_mar)

# En python, tipo de variable son dinamicos, los que significa que una variable puede 
# cambiar de tipo durante la ejecucion del program. por ejemplo: 
edad = "Venticinco" # Ahora la variable edad es de tipo cadena de texto (str)
print("\nValor actualizado de edad :", edad) 

telefono = None # la variable telefono se inicializa con el valor None, que representa la ausencia de valor
print("\nTelefono :", telefono )

# Si queremos acceder a una variable no declarada previamente, python mostrara un error de tipo name error, 
# indicando que la variable no esta definida. por ejemplo: 
telefono = "1234567890" #se asigna un valor a la variable telefono
print("\nTelefono :", telefono)
