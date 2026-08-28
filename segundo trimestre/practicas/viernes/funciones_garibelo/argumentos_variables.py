print("*** Argumentos Variables ***")

#definimos la funcion

def superheroe_superpoderes(superheroe,nombre,*args):
    print(f"Superheroe: {superheroe}- {nombre} - {args}")
    lista_poderes = []
    for n in args:
        lista_poderes.append(n)
    print(f"Los poderes de {superheroe} son: {lista_poderes}\n")
    
superheroe_superpoderes("Spiderman","Piter Parker","Instinto Aracnido","Telaraña")
superheroe_superpoderes("Iron Man","Tony Stark","El hombre de hierro","Multimillonario","Genio","Playboy","Filantropo")
