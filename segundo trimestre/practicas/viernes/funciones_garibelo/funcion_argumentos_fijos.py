#funcion llamada persona creando parametros "nombre "apellido", "edad"
def persona(nombre, apellido, edad):
    print(f'Su nombre es {nombre} {apellido} y tiene {edad} años ')

persona("Juan", "Hernandez", "21")


#funcion llamada "funcion_persona" tres parametros nombre apellido edad y que los argumentos cundo se llame la funcion los muestre en mayucula 
def funcion_persona(nombre, apellido, edad):
    print(f'Su nombre es {nombre} {apellido} y tiene {edad} años '.upper())

funcion_persona("Carlos", "Ramirez", "19")



def perosna_mayuscula(nombre, apellido, edad):
    return nombre.upper(), apellido.upper(), edad

#llamamos la funcion perosna_mayuscula con los tres argumentos
#utlizamos la tecnia llamda desempaquetaod de tupla o un unpacking

nombre, apellido, edad= perosna_mayuscula("sandra", "jimenez", 42)

print(f'Resultado de persona: nombre= {nombre}, apellido= {apellido}, edad= {edad} ')

def persona_mayuscula(nombre,apelldio,edad):
    nombre,apelldio = nombre.upper(), apelldio.upper()
    return f"Su nombre en mayuscula es {nombre}. Su apellido en mayuscula es: {apelldio}, con su edad: {edad}"

print(persona_mayuscula(input('DIgite su nombre:'),input('Digite su apellido: '),int(input('Digite su edad: '))))

def obtener_coordenadas(x,y,z):
    return x,y,z
resultado = obtener_coordenadas(15,25,35)
x1, y1, z1 = resultado 
print(y1)
