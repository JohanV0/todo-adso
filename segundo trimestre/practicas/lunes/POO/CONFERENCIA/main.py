from Conferencia import Conferencia
from Asistente import Asistente
def simulador():
    persona1 = Asistente(nombre="Juan Pedro Morales", correo="juanpedro@gmail.com")
    conferencia1 = Conferencia(titulo="hola mundo", hora="10:00 am")
    persona2 = Asistente(nombre="Paula Isabella Girón", correo="paulagiron@gmail.com")
    conferencia2 = Conferencia(titulo="hola mundo bienvenido al nuevo mundo", hora="12:00 pm")
    persona3 = Asistente(nombre="Paula Isabella Girón", correo="paulagiron@gmail.com")
    persona4 = Asistente(nombre="Paula Isabella Girón", correo="paulagiron@gmail.com")

    print(conferencia1.registro_de_asistente(persona1))
    print(conferencia1.registro_de_asistente(persona2))
    print(conferencia1.lista_asistente())

    print(conferencia2.registro_de_asistente(persona3))
    print(conferencia2.registro_de_asistente(persona4))
    print(conferencia2.lista_asistente())
    

if __name__ == "__main__":
    simulador()