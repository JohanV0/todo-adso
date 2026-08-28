def calcular_pago(horas_tabajadas,valor_hora):
    if horas_tabajadas <= 40:
        pago = horas_tabajadas * valor_hora
        return pago
    elif horas_tabajadas > 40:
        pago_normal = 40 * valor_hora
        pago = ((horas_tabajadas-40) * 0.25) + pago_normal
        return pago
def calcular_total_nomina(lista_personas):
    total_nomina = sum(lista_personas)
    return total_nomina

persona1 = calcular_pago(int(input('Digite las horas trabajadas: ')), float(input('Digite el valor por hora: ')))
persona2 = calcular_pago(int(input('Digite las horas trabajadas: ')), float(input('Digite el valor por hora: ')))
persona3 = calcular_pago(int(input('Digite las horas trabajadas: ')), float(input('Digite el valor por hora: ')))
persona4 = calcular_pago(int(input('Digite las horas trabajadas: ')), float(input('Digite el valor por hora: ')))

lista_persona = [persona1, persona2, persona3, persona4]
total_nomina = calcular_total_nomina(lista_persona)
print(f'''
Total a pagar a persona1: {persona1}
Total a pagar a persona1: {persona2}
Total a pagar a persona1: {persona3}
Total a pagar a persona1: {persona4}
Total de pagar nomina: {total_nomina}
''')