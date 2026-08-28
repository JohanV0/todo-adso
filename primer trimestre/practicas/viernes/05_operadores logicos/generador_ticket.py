print('generador de tickets: ')
producto_1=float(input("ingrese el valor del primer producto: (con decimal)"))
producto_2=float(input("ingrese el valor del segundo producto: (con decimal)"))
producto_3=float(input("ingrese el valor del tercero producto: (con decimal)"))
producto_4=float(input("ingrese el valor del cuarto producto: (con decimal)"))
descuento=int(input("cuanto quiere de descuento?: (con entero)"))

max_descuento = 10 
IVA=0.19

subtotal=(producto_1+producto_2+producto_3+producto_4)
total=subtotal*IVA

total_descuento=total*descuento

print(f'''\t\tGenerador De Tickets 
      subtotal: {subtotal}
      total: {total:.2f}
      total con descuento: {total_descuento}
      ''')