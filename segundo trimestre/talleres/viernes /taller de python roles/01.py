print('Bienvenido al Duelo de Magos')
nombre_jugador1 = input('Jugador 1 porfavor digite su nombre: ')
hechizo_jugador1 = input(f'¿Jugador {nombre_jugador1} que tipo de hechizo quiere usar (Fuego/Agua/Tierra)?: ').lower().strip()
print(f'\n turno del jugador 2')
nombre_jugador2 = input('Jugador 2 porfavor digite su nombre: ')
hechizo_jugador2 = input(f'¿Jugador {nombre_jugador2} que tipo de hechizo quiere usar (Fuego/Agua/Tierra)?: ').lower().strip()

hechizos_permitidos = 'agua','tierra','fuego'
FUEGO = 30
AGUA = 20
TIERRA = 25
VIDA_JUGADOR1= 100
VIDA_JUGADOR2= 100

if hechizo_jugador1 == "fuego" in hechizos_permitidos and hechizo_jugador2 == "tierra" in hechizos_permitidos:
    puntaje = FUEGO - TIERRA
    VIDA_JUGADOR2 = VIDA_JUGADOR2 - puntaje
    print(f'''
    El jugador {nombre_jugador1} con el hechizo {hechizo_jugador1} le gana al jugador {nombre_jugador2} que eligio {hechizo_jugador2}
    {hechizo_jugador1}  = {FUEGO} 
    {hechizo_jugador2} = {TIERRA}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}:{VIDA_JUGADOR2}
''')

elif hechizo_jugador1 == "tierra" in hechizos_permitidos and hechizo_jugador2 == "fuego" in hechizos_permitidos:
    puntaje = FUEGO - TIERRA
    VIDA_JUGADOR1 = VIDA_JUGADOR1 - puntaje
    print(f'''
    El jugador {nombre_jugador2} con el hechizo {hechizo_jugador2} le gana al jugador {nombre_jugador1} que eligio {hechizo_jugador1}
    {hechizo_jugador2} = {FUEGO}
    {hechizo_jugador1} = {TIERRA}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}:{VIDA_JUGADOR2}''')

elif hechizo_jugador1 == "tierra" in hechizos_permitidos and hechizo_jugador2 == "agua" in hechizos_permitidos:
    puntaje = TIERRA - AGUA
    VIDA_JUGADOR2 = VIDA_JUGADOR2 - puntaje
    print(f'''El jugador {nombre_jugador1} con el hechizo {hechizo_jugador1} le gana al jugador {nombre_jugador2} que eligio {hechizo_jugador2}
    {hechizo_jugador1}  = {TIERRA} 
    {hechizo_jugador2} = {AGUA}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}: {VIDA_JUGADOR2}''')

elif hechizo_jugador1 == "agua" in hechizos_permitidos and hechizo_jugador2 == "tierra" in hechizos_permitidos:
    puntaje = TIERRA -AGUA
    VIDA_JUGADOR1 = VIDA_JUGADOR1 - puntaje
    print(f'''El jugador {nombre_jugador2} con el hechizo {hechizo_jugador2} le gana al jugador {nombre_jugador1} que eligio {hechizo_jugador1}
    {hechizo_jugador2} = {TIERRA}
    {hechizo_jugador1} = {AGUA}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}: {VIDA_JUGADOR2}''')

elif hechizo_jugador1 == "agua" in hechizos_permitidos and hechizo_jugador2 == "fuego" in hechizos_permitidos:
    puntaje = FUEGO - AGUA
    VIDA_JUGADOR2 = VIDA_JUGADOR2 - puntaje  
    print(f'''El jugador {nombre_jugador1} con el hechizo {hechizo_jugador1} le gana al jugador {nombre_jugador2} que eligio {hechizo_jugador2}
    {hechizo_jugador2} = {FUEGO}
    {hechizo_jugador1} = {AGUA}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}: {VIDA_JUGADOR2}''')

elif hechizo_jugador1 == "fuego" in hechizos_permitidos and hechizo_jugador2 == "agua" in hechizos_permitidos:
    puntaje = FUEGO -AGUA
    VIDA_JUGADOR1 = VIDA_JUGADOR1 - puntaje
    print(f'''El jugador {nombre_jugador2} con el hechizo {hechizo_jugador2} le gana al jugador {nombre_jugador1} que eligio {hechizo_jugador1}
    {hechizo_jugador2} = {AGUA}
    {hechizo_jugador1} = {FUEGO}
    total = {puntaje}
    VIDA DEL JUGADOR {nombre_jugador1}: {VIDA_JUGADOR1}
    VIDA DEL JUGADOR {nombre_jugador2}: {VIDA_JUGADOR2}''')

elif hechizo_jugador1 == hechizo_jugador2:
    print(f'Empate glorioso. Ambos magos son dignos rivales.')

elif hechizo_jugador1 != hechizos_permitidos or hechizo_jugador2 != hechizos_permitidos:
    print(f'Jugador {nombre_jugador1} el hechizo "{hechizo_jugador1.upper()}" no es permitido, por favor elija entre {hechizos_permitidos}')


