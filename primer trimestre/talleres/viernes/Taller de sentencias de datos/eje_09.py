peso = float(input('Digite su peso actual en kg: '))
altura = float(input('Digite su estatura actual: '))

IMC = peso / altura**2

print(''''
______________________________________________________________________
|                                 |                                  |
|          Menor de 16,5          |       Bajo de peso severo        |
|_________________________________|__________________________________|
|                                 |                                  |
|          Menor de 18,5          |           Bajo de peso           |
|_________________________________|__________________________________|
|                                 |                                  |
|            18,5-24,9            |            Normopeso             |
|_________________________________|__________________________________|
|                                 |                                  |
|             25-26,9             |         Sobrepeso grado I        |
|_________________________________|__________________________________|
|                                 |                                  |
|             27-29,9             |         Sobrepeso grado II       |
|_________________________________|__________________________________|
|                                 |                                  |
|             30-34,9             |          Obesidad Tipo I         |
|_________________________________|__________________________________|
|                                 |                                  |
|             35-39,9             |          Obesidad Tipo II        |
|_________________________________|__________________________________|
|                                 |                                  |
|             40-49,9             |    Obesidad Tipo II(morbida)     |
|_________________________________|__________________________________|
''')

if IMC <= 16.5:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Bajo de peso severo')
elif IMC <18.5:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Bajo de peso')
elif IMC >= 18.5 and IMC <= 24.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Normpeso')
elif IMC >= 25 and IMC <= 26.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Sobrepeso I')
elif IMC >= 27 and IMC <= 29.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Sobrepeso II')
elif IMC >= 30 and IMC <= 34.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Obesidad Tipo I')
elif IMC >= 35 and IMC <= 39.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Obesidad Tipo II')
elif IMC >= 40 and IMC <= 49.9:
    print(f'Su IMC es de {IMC:.1f} por lo que tiene Obesidad Tipo II(morbida)')
else:
    print(f'ingrese un valor correcto')