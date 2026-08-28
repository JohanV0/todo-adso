     #Archivo         #Clase
from Pasajero import Pasajero
from Conductor import Conductor
from Viaje import Viaje 

def ejecutar_sistema():
    print('=== Inicializando Sitema SWIFTRIDE')
    
    pasajero = Pasajero(nombre="Johan Andres", telefono="3113049045", nombre_empresa="TechInnovate S.A", tiene_credito=True)
    conductor = Conductor(nombre="Ana Gomez", licencia="1110012551", calificacion=4.8, modelo_vehiculo="Toyota Corona 2004", placa="XYZ123")
    viaje = Viaje(origen="Aeropuerto Perales", destino="Hotel Eestelar", costo=55000.0, distancia=8)
    print("--- Resumen de operación---")
    print(f'Pasajero Corporativo {pasajero.nombre} de {pasajero.nombre_empresa}')
    print(f'Conductor asignado {conductor.nombre} de {conductor.placa}')
    print(f'Ruta asignada {viaje.origen} -> {viaje.destino}')
    print(f'costo del servicio {viaje.costo}')
    print(f'='*40)

if __name__ == "__main__":
    ejecutar_sistema()
    