aprendices_mañana = [ "Carlos Ramos", "Laura Ospina", "Andrés Gómez", "Valentina Cruz", "Diego Vargas", "Sofía Valencia", "Miguel Torres"]
aprendices_tarde = ["Laura Ospina", "Felipe Arango", "Camila Herrera", "Diego Vargas", "Juliana Pérez", "Andrés Gómez", "Ricardo Muñoz" ]

iguales = set(aprendices_mañana) & set(aprendices_tarde)
solo_aprendices_mañana = set(aprendices_mañana) - set(aprendices_tarde)
solo_aprendices_tarde = set(aprendices_tarde) - set(aprendices_mañana) 
total_aprendices_unicos = solo_aprendices_mañana | solo_aprendices_tarde
print(f"Los que son iguales: {iguales}")
print(f"Solo los de la mañana :{solo_aprendices_mañana}")
print(f"Solo los de la tarde {solo_aprendices_tarde}")
print(f"Total los unicos: {total_aprendices_unicos}")
