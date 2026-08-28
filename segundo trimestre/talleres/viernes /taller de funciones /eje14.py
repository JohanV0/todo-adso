
def calcular_descuento(monto, es_miembro):
    if monto < 100000:
        return 0
    elif monto < 300000:
        if es_miembro:
            return 10
        return 5
    elif monto < 600000:
        if es_miembro:
            return 15
        return 10
    else:
        if es_miembro:
            return 20
        return 15

def aplicar_descuento(monto, descuento):
    return monto - (monto * descuento / 100)

total_compras = 0
total_descuentos = 0

while True:
    dato = input("Monto de compra (digite salir para terminar): ")
    if dato.lower() == "salir":
        break
    monto = float(dato)
    miembro = input("Es miembro? (si/no): ").lower()
    if miembro == "si":
        es_miembro = True
    else:
        es_miembro = False
    descuento = calcular_descuento(monto, es_miembro)
    valor_final = aplicar_descuento(monto, descuento)
    descuento_otorgado = monto - valor_final
    total_compras += valor_final
    total_descuentos += descuento_otorgado

    print(f"""
    Descuento: {descuento}%
    Valor final:{valor_final}""")

print("RESUMEN")

print(f"""
    Total vendido: {total_compras}
    Total descuentos: {total_descuentos})
""")