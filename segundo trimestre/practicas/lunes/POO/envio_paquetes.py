'''
Cree un programa que calcule el costo total de enviar un paquete internacional. Debe incluir 3 funciones secundadrias y una principal

1. calcular_impuesto(peso) -> Por cada kilo cobran 5 dolares. Devuelve el costo base.
2.calcular_costo(distancia) -> Si la distancia es mayor a 1.000km, se cobra un recargo fijo de 20 dolares. Si no, no hay recargo
3. aplicar_impuesto(subtotal) ->Añade 5% de impuesto al subtotal recibido.
4.simulador_envio() -> Funcion principal. Pide al usuario por consola el peso del paquete y la distancia. Llama a las 3 funciones anteriores en orden para calcular el precio final y muestra el desgloce en pantalla
'''

peso = 0 
distancia = 0 
subtotal = 0
def calcular_impuesto(peso):
    peso = (peso / 1000)* 5
    subtotal = peso
    return subtotal

def calcular_costo(distancia):
    if distancia > 10000:
        subtotal += 20
        return subtotal
def aplicar_impuesto(subtotal):
    subtotal *= 1.05
    return subtotal
def simulador_envio():
    peso = float(input('Digite el peso del producto en "gr": '))
    distancia = int(input('Digite la distancia: '))
    total = calcular_impuesto + calcular_costo + aplicar_impuesto
    print(f'El costo por peso es de: {calcular_impuesto(peso)}')
    print(f'El costo por peso es de: {calcular_costo(distancia)}')
    print(f'El costo por peso es de: {aplicar_impuesto(subtotal)}')
    print(f'El costo totales de : {total}')
print(simulador_envio())