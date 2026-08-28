seg = int(input('digite los segundos: '))
hora = seg / 36000
residuo_hora = seg % 36000
minu = residuo_hora / 60 
seg_nuevos = residuo_hora % 60 

print(f'{hora}:{minu}:{seg_nuevos}')