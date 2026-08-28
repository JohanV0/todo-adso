print('Ejemplo de break')

for i in range(1,10):
    if i == 5:
        break
    print(i, end=' ')

print('\nEjemplo de continue')

for i in range(1,21):
    if i == 10 and i == 18:
        continue
    print(i, end=' ')