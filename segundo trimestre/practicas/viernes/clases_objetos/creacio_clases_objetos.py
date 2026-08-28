class Persona:
    def inicializar_persona(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_persona(self):
        print(f'''
    Persona: 
    - Nombre: {self.nombre}
    - Apellido: {self.apellido}''')
        
if __name__ == "__main__":
    persona1 = Persona()
    persona1.inicializar_persona('layla','gimenez')
    persona1.mostrar_persona()