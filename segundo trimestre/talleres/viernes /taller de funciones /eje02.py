def calcular_iva(valor,categoria):

    IVA = 0.19

    if valor is not float(valor):
        return "Valor tiene que ser float"
    elif categoria == 'si':
        IVA = 0
        return (valor * IVA),(valor + (valor * IVA))
    else:
        return (valor * valor_base),(valor + (valor * valor_base))
    
valor_ingresado = input('Digite el valor base del producto: ')
valor_numerico = float(valor_ingresado)
canasta_basica = input('Su categoria esta en canasta_basica?(si/no): ').lower().strip()
valor_base , valor_total = calcular_iva(valor_numerico,canasta_basica)

print(f'Valor Base: {valor_numerico}')
print(f'Valor Base con IVA: {valor_base}')
print(f'Valor Total: {valor_total}')