# def suma(*args):
#     sumar = sum(args)
#     return sumar
# resultado = suma(1,2,3,4,5,6,7,8,9,10)
# print(resultado)

#2.ejercicio

def imprimir_detalle_persona(**kwargs):
    print("\n*** Impirmir detalles de una persona usando kwargs ***")
    for j,c in kwargs.items():
        print(f"-{j} | {c}")

persona1 = imprimir_detalle_persona(nombre = "Juan Gomez", edad = 19, ciudad = "Ibague")
persona2 = imprimir_detalle_persona(nombre = "Johan Vergara", edad = 18, ciudad = "Bogota", puesto = "Programador")
