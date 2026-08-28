class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_persona(self):
        print(f'''
    Persona: 
    - Nombre: {self.nombre}
    - Apellido: {self.apellido}''')
persona1 = Persona('Goooooooooooooool','Caracol')
persona1.mostrar_persona()

