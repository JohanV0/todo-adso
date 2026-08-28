from Mascota import Mascota
from Persona import Persona
def simulador():
    persona1 = Persona(nombre="Juan Pedro Morales", edad=29)
    persona2 = Persona(nombre="Paula Isabella Girón", edad=14)

    perrito = Mascota(nombre="Firulais", especie = "Perro")
    gatito = Mascota(nombre="Motita", especie = "Gato")
    loro = Mascota(nombre="Manolo", especie = "Loro")

    print(persona1.agregar_mascota(perrito))
    print(persona1.listar_mascotas())

    print(persona2.agregar_mascota(gatito))
    print(persona2.agregar_mascota(loro))
    print(persona2.listar_mascotas())

if __name__ == "__main__":
    simulador()
    