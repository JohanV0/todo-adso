from MiembroEspacial import MiembroEspacial
from Piloto import Piloto
from Cohete import Cohete
from Mision import Mision

cohete = Cohete("Halcón 9", 45.5, "Raptor V2", 2200.0)
print(cohete.calcular_aceleracion_estimada())  

# 2. Crear un piloto
piloto = Piloto("Ana", 28, "Comandante", 600)
piloto1 = Piloto("johan", 2, "Comandante", 600)
piloto2 = Piloto("Andres", 3, "Comandante", 600)
piloto3 = Piloto("Vergara", 4, "Comandante", 600)
piloto4 = Piloto("Robledo", 28, "Comandante", 600)
piloto5 = Piloto("Ana", 28, "Comandante", 600)
piloto6 = Piloto("Ana", 28, "Comandante", 600)
piloto7 = Piloto("Ana", 28, "Comandante", 600)
print(piloto.presentarse())          
print(piloto.es_apto_para_mision())  

# 3. Crear la misión, uniendo cohete + piloto
mision = Mision("Apolo", "Luna", cohete)
mision.agregar_miembro(piloto)
mision.agregar_miembro(piloto1)
mision.agregar_miembro(piloto2)
mision.agregar_miembro(piloto3)
mision.agregar_miembro(piloto4)
mision.agregar_miembro(piloto5)
mision.agregar_miembro(piloto6)
mision.agregar_miembro(piloto7)

# 4. Revisar que el tripulante se agregó bien
print(mision.lista_miembro())