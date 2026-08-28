from Futbolista import Futbolista
from Cuerpo_Tecnico import CuerpoTecnico

def simulador_concentracion():
    print("// Concentracion de la seleccion Colombia - Mudial 2026 //")

    el_diez = Futbolista('James Rodriguez','COL123456788',10,'Volante')
    crack = Futbolista('Luiz Dias','COL38764131',7,'Extremo Izquierdo')
    el_profe = CuerpoTecnico('Nestor Lorenzo','ARG13354444',"Director Tecnico",15)

    el_diez.viajar("Kansas City")
    crack.viajar("Kansas City")
    el_profe.viajar("Kansas City")

    print('--- Inicia el partido de 16avos de final ---')
    crack.jugar_partido()
    el_diez.jugar_partido()
    el_profe.dar_instrucciones()

if __name__ == "__main__":
    simulador_concentracion()