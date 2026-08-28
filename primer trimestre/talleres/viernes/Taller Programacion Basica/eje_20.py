CREDENCIAL= bool(input('Tiene credencial de la biblioteca ?: ').lower().strip() == 'si')
CERCA_BIBLIOTECA= bool(input('Vive cerca de la biblioteca?: ').lower().strip() == 'si')

prestamo = CREDENCIAL == 'si' and CERCA_BIBLIOTECA == 'si'
print(f'''
    Cumple conn las condiciones para el prestamo de un libro? {prestamo}''')