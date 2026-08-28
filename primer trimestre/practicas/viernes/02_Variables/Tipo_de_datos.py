 # Ejemplo de tipo de datos en python 

# Tipo de dato entero (int)
edad = 25
print ("Edad:", edad)

# Tipo de dato flotante (float)
altura = 1.75
print ("Altura:", altura)

# Tipo de dato cadena de texto (str)
nombre = "Juan perez"
print ("Nombre:", nombre)

# Tipo de dato booleano (bool)
es_estudiante = True
print ("Es_estudiante:", es_estudiante)

# Tipo de dato None (NoneType)
direccion = None #variable que respresenta la ausencia de un valor 
print ("Direccion:", direccion)

# Para detectar automaticamente el tipo de dato de una variable segun el valor que se le asigna. 
# por ejemplo, si asignamos un numeor entero a una variable, python la tratara como un entero (int). Si asignamos 
# una cadena de text, python la tratara como una cadena (srt), y asi sucesivamnete. 

print("\n Tipo de datos de cadena variable : ")
print("Tipo de dato de edad :", type(edad)) # Muestra <class 'int'>

print("\n Tipo de datos de cadena variable : ")
print("Tipo de dato de altura :", type(altura)) # Muestra <class 'float'>

print("\n Tipo de datos de cadena variable : ")
print("Tipo de dato de Nombre :", type(nombre)) # Muestra <class 'str'>

print("\n Tipo de datos de cadena variable : ")
print("Tipo de dato de Es_estudiante :", type(es_estudiante)) # Muestra <class 'bool'>

print("\n Tipo de datos de cadena variable : ")
print("Tipo de dato de Direccion :", type(direccion)) # Muestra <class 'Nonetype'>


