def es_valida(password):
    pasa = False
    if password is not str and len(password) > 8:
        for n in password:
            if n.isdigit() == True:
                pasa = f'True. La contraseña si fue aprobada'
            else:
                pasa = f'False. Necesita llevar un numero'
        return pasa
    else:
        return f'{pasa}. Debe llevar minimo 8 caracteres'
    
password = input('Digite su contraseña: ')
print(f'Contraseña propuesta por el usuario: {password}')
print(f'La contraseña fue aceptada?: {es_valida(password)}')