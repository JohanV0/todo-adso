
# Encuesta de satisfacción - TECNOZONE
# Lista de 20 calificaciones (1-5)
respuestas = [5, 3, 4, 2, 1, 5, 4, 3, 2, 5, 1, 4, 3, 5, 2, 4, 1, 3, 5, 2]

positivas = []
negativas = []
for n in respuestas:
    if n >= 4:
        positivas.append(n)
for n in respuestas:
    if n <= 2:
        negativas.append(n)
porcentaje_positivas = len(positivas)/len(respuestas)*100
porcentaje_negativas = len(negativas)/len(respuestas)*100

frecuencia = {}
for i in respuestas:
    frecuencia[i] = frecuencia.get(i,0) + 1

moda = max(frecuencia, key=frecuencia.get)
minimo = min(frecuencia, key=frecuencia.get)

histograma = {}
for j in respuestas:
    histograma[j] = histograma.get(j, '█') + '█'
print(f'Total de respuestas: {len(respuestas)}')
print(f'Total de respuestas positivas: {len(positivas)}')
print(f'Total de respuestas negativas: {len(negativas)}')
print(f'Calificacion maxima: {moda}')
print(f'Calificacion minima: {minimo}')
print(f'Histograma: ')
for h,b in histograma.items():

    print(f'{h} : {b}')