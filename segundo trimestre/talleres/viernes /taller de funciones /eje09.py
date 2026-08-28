def agregar_producto(dic,catalogo,nom_producto):
    if catalogo not in dic:
        dic[catalogo] = []
        dic[catalogo].append(nom_producto)
    else:
        dic[catalogo] = nom_producto
    for c,j in dic.items():
        for d in j:
            continue
    return dic
def contar_por_categoria(dic):
    for c,j in dic.items():
        valor = 0
        for d in j:
            valor += 1
        print(f'{c} -> {valor}')
            
    return 

productos = {
    "Tecnología": [
        "Laptop",
        "Mouse",
        "Teclado",
        "Monitor"
    ],
    "Alimentos": [
        "Arroz",
        "Leche",
        "Pan",
        "Huevos"
    ],
    "Ropa": [
        "Camisa",
        "Pantalón",
        "Chaqueta",
        "Zapatos"
    ],
    "Aseo": [
        "Jabón",
        "Champú",
        "Crema dental",
        "Papel higiénico"
    ],
    "Papelería": [
        "Cuaderno",
        "Lápiz",
        "Borrador",
        "Regla"
    ]
}
nuevo_categoria = input('Digite el nombre de la categoria: ')
nombre_nuevo_producto = input('Digite el nombre del nuevo producto: ')
nuevo_producto = agregar_producto(productos,nuevo_categoria,nombre_nuevo_producto)
print(contar_por_categoria(nuevo_producto))