calificacion = int(input('ingrese una calficacion de (0 a 100): '))
if calificacion >= 90 and calificacion <= 100:
    print(f'su calificacion es A')
elif calificacion >= 80 and calificacion <= 89:
    print(f'su calificacion es B')
elif calificacion >= 70 and calificacion <= 79:
    print(f'su calificacion es C')
elif calificacion >= 60 and calificacion <= 69:
    print(f'su calificacion es D')
elif calificacion >= 0 and calificacion <= 59:
    print(f'su calificacion es F')
else:
    print('el numero ingresado no esta entre (0/100)')