print("*** Argumentos variables en forma de dict ***")

# definimos una funcion 

def superheroe_superpoderes(nombre,*args,**kwargs):
    print(f"Superheroe: {nombre} - {args} - Mas Info: {kwargs}")
superheroe_superpoderes("Spiderman", "Instinto Aracnido", edad=17,empresa="marvel")
superheroe_superpoderes("Iron Man","Tony Stark","El hombre de hierro","Multimillonario","Genio","Playboy","Filantropo",edad=34,empresa="Marvel")
