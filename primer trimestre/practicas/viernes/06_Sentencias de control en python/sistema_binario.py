aceptacion  =  bool(input('desea continuar con el sistema?: ').strip().upper()=="NO")
aceptacion = not aceptacion
if aceptacion == False:
    print('Continuamos en el sistema')
else:
    print('saliendo del sisttema')
