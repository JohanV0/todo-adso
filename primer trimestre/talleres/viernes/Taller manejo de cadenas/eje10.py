nom_proveedor=input("nombre del proveedor: ")
num_productos=int(input("cantidad de productos suministrados: "))
monto=float(input("monto total: "))
proveedor=bool(input("¿el proveedor esta activo?: ")=="si")

print(f' nombre del proveedor: {nom_proveedor} \n numero de productos suministrados: {num_productos} \n monto total de la factura: {monto} \n Estcado del proveedor: {proveedor}') 