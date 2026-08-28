print("*** ALcance Variables***")

#Declarar variable global
contador_global = 0

def incrementar_contador():
    contador_local = 0
    
    global contador_global 
    contador_global += 1 
    contador_local += 1

    print(f"contador local: {contador_local}")
    print(f"contador global: {contador_global}")

incrementar_contador()
incrementar_contador()