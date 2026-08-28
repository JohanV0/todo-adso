nombre = input("Ingresa tu nombre: ").strip().lower().title()
print(f'''{nombre}, este es tu testamento.
solo hace falta que indiques la division de tu fortuna.''')

herederos  = int(input(f'\n{nombre}, indica la cantidad de herederos: '))
fortuna= float(input('Ahora indica tu fortuna total: '))

CANTIDAD = fortuna // herederos
CARIDAD = fortuna % herederos
IMPUESTO  = 0.22
IMPUESTO_HERENCIA =  CANTIDAD * IMPUESTO
COBRAR_HERENCIA = CANTIDAD - IMPUESTO_HERENCIA
IMPUESTO_CARIDAD = CARIDAD * IMPUESTO
COBRAR_CARIDAD = CARIDAD -IMPUESTO_CARIDAD

print(f'''El total de ${fortuna} se distribuira como sigue: 
    HEREDEROS: {herederos}
    C/U RECIBE= {CANTIDAD}
    A CARIDAD: {CARIDAD:.0f}''')

print(f'''\nSe ha de grabar todo con el impuesto a la ganancia de 22$: 
    POR HERENCIA   {CANTIDAD}  IMPUESTO=   {IMPUESTO_HERENCIA:.2f}    A COBRAR:    {COBRAR_HERENCIA:.2f}
    A CARIDAD   {CARIDAD:.0f}  IMPUESTO=   {IMPUESTO_CARIDAD:.2f}    A COBRAR:    {COBRAR_CARIDAD:.2f}''')