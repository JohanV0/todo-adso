
horas = float(input('Ingrese las horas de trabajo: '))#Se guardan las horas que se trabajaron
valor_horas = float(input('Ingrese el valor por hora '))#Se ingresa el valor por hora 
if horas < 48 and  horas > 0:#Se hace un rango de 0 a 48
    horas_normal = valor_horas / horas#Se saca el valor de cada hora
    print(f'Su salario por hora es de: {horas_normal:.2f}')#Se muestra el salario por hora con dos decimales 
elif horas == 0:#Si no tiene horas no tiene salario
    print(f'Su salario es de: 0')
elif horas > 48:#Se saca el salario si sus horas son mayores a 48 con un 1.75 mas y se muestra 
    horas_normal = valor_horas / horas
    horas_extras = horas_normal + 1.75
    print(f'Su salario es de: {horas_extras:.2f}')
elif horas < 0:#NO cuenta si es menor a cero 
    print(f'El valor ingresado no puede ser 0')
else:
    print('El valor ingresado no es valido')#Si se ingresa un valor diferente a 0 