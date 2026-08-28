contraseña = input("Crea tu contraseña(minimo 8 caracteres)")
#validar longitud
es_larga = False

if contraseña[0:1] != "":
    largo = 1
else:
    largo = 0
if contraseña[1:2] != "":
    largo+=1
if contraseña[2:3] != "":
    largo+=1
if contraseña[3:4] != "":
    largo+=1
if contraseña[4:5] != "":
    largo+=1
if contraseña[5:6] != "":
    largo+=1
if contraseña[6:7] != "":
    largo+=1
if contraseña[7:8] != "":
    largo+=1
if contraseña[8:9] != "":
    largo+=1
    if largo>=8:
        es_larga=True
if contraseña[0:1] != contraseña[0:1].lower():
    tiene_mayuscula = True
elif contraseña[1:2] != contraseña[1:2].lower():
    tiene_mayuscula = True
elif contraseña[2:3] != contraseña[2:3].lower():
    tiene_mayuscula = True
elif contraseña[3:4] != contraseña[3:4].lower():
    tiene_mayuscula = True
elif contraseña[4:5] != contraseña[4:5].lower():
    tiene_mayuscula = True
elif contraseña[5:6] != contraseña[5:6].lower():
    tiene_mayuscula = True
elif contraseña[6:7] != contraseña[6:7].lower():
    tiene_mayuscula = True
elif contraseña[7:8] != contraseña[7:8].lower():
    tiene_mayuscula = True
elif contraseña[8:9] != contraseña[8:9].lower():
    tiene_mayuscula = True

if contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
    
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
elif contraseña[0:1] =="0" or contraseña[0:1] == "1" or contraseña[0:1] == "2" or contraseña[0:1] == "3" or contraseña[0:1] == "4" or contraseña[0:1] == "5" or contraseña[0:1] == "6" or contraseña[0:1] == "7" or contraseña[0:1] == "8" or contraseña[0:1] == "9":
    tiene_numero = True
