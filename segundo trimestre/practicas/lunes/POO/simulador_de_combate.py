import random 

#heroe:
def calcular_ataque_heroe():
    return random.randint(15,30)
def calcular_defensa_heroe():
    return random.randint(10,20)

#monstruo:
def calcular_ataque_monstruo():
    return random.randint(15,30)
def calcular_defensa_monstruo():
    return random.randint(10,20)

def simular_turno():

    print('-' * 50)
    print('Bienvenido al juego del heroe contra el monstruo.')
    print('-' * 50)
    vida_heroe = 30
    vida_monstruo = 30
    ronda = 0
    continuar = input('Digite enter para comenzar o continuar ronda: ')
    if continuar == "":
        while vida_heroe > 0 or vida_monstruo > 0:

            ataque_heroe = calcular_ataque_heroe()
            defensa_heroe = calcular_defensa_heroe()

            ataque_monstruo = calcular_ataque_monstruo()
            defensa_monstruo = calcular_defensa_monstruo()

            daño_final_heroe = ataque_heroe - defensa_monstruo
            daño_final_monstruo = ataque_monstruo - defensa_monstruo

            vida_heroe -= daño_final_monstruo
            vida_monstruo -= daño_final_heroe

            ronda += 1
            print(f'Ronda: {ronda}')
            if vida_heroe != 0 and vida_monstruo != 0:
                print(f'En esta impresionante pelea el heroe hace un daño de {ataque_heroe}. Es impresionante el monstruo logra defenderse con un {defensa_monstruo} pero al final el \ndaño del heroe es mas grande y provoca {daño_final_heroe} puntos de daño, la vida del monstruo queda con un total de {vida_monstruo} puntos de vida restante.\nEl monstruo ataca y hace un daño de {ataque_monstruo}.El heroe logra defenderse con un {defensa_heroe} pero al final el daño del heroe es mas grande y provoca {daño_final_monstruo} puntos de daño, la vida del heroe queda con un total de {vida_heroe} puntos de vida.')
            if vida_heroe == 0:
                print('Tristemente me toca contarles, que nuestro heroe #1 murio a manos del monstruo y no tenemos escapatoria.')
                break
            elif vida_monstruo == 0:
                print('Tenemos noticias de ultima hora, el heroe dando todo de si, logro acabar con el monstruo despues de una dura pelea, muchas gracias heroe, esta ciudad no seria nada sin usted.')
                break
simular_turno()