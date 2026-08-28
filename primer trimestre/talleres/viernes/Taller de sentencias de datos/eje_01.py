edad = int(input('digite su edad: '))
salario = float(input('Ingrese su salario mensual: '))
edad_min = 18
edad_max = 65
salario_min = 1200000
salario_bonus = 5000000
if edad >= edad_min and edad <= edad_max and salario >= salario_min and salario <= salario_bonus:
    print(f'usted hace es posible hacerle el pago')
elif  edad >= edad_min and edad <= edad_max and salario > salario_bonus:
    print(f'usted califica para el prestamo premium')
else:
    print(f'usted no califica para el prestamo')