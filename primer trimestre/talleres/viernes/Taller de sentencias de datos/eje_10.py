salario_anual = float(input(f'Ingrese su salario anual'))

breakpoint()

if salario_anual < 30000000:
    print(f'usted no paga impuestos')
elif salario_anual >= 30000000 and salario_anual <= 50000000:
    impuesto_anual = salario_anual * .1
    pago_anual = salario_anual - impuesto_anual
    print(f'usted paga en total: {pago_anual}')
elif salario_anual > 50000000:
    impuesto_anual = salario_anual * .2
    pago_anual = salario_anual - impuesto_anual
    print(f'usted paga en total: {pago_anual}')