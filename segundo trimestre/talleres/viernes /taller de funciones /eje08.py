def es_palindromo(texto):
    contenedor_valor = ''
    for n in reversed(texto):
        valor = str(n)
        contenedor_valor += valor
    if contenedor_valor == texto:
        es_palindromo = True
    else:
        es_palindromo = False

    return es_palindromo
def contar_palindromos_lista(texto):
    lista_palindromos = []
    for n in texto:
        if es_palindromo(n) == True:
            lista_palindromos.append(n)
    return lista_palindromos

palabras = [
    "ana",         
    "reconocer",   
    "radar",       
    "oso",         
    "salas",       
    "somos",       
    "python",      
    "computador",  
    "programacion",
    "teclado",     
    "monitor",     
    "sena",        
    "nivel",       
    "rotor",       
    "casa",        
    "sol"          
]

print(contar_palindromos_lista(palabras))