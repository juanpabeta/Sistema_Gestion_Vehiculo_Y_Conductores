from models.motor import Motor
from models.conductor import Conductor
from models.moto import Moto
from models.carro import Carro
from models.camion import Camion
from models.vehiculo import Vehiculo
from services.gestionVehiculos import GestionVehiculos


def mostrarInfoVehiculo(vehiculo) -> None:
    print("="*50)
    print("Información del Vehículo")
    print("="*50)
    print(" Tipo: ", type(vehiculo).__name__)
    print(" Placa:", vehiculo.placa)
    print(" Marca:", vehiculo.marca)
    print(" Estado:", vehiculo.estado)
    print(" Tipo de motor:", vehiculo.motor.tipo)
    print(" Velocidad del motor:", vehiculo.motor.velocidad)
    print(" Motor encendido:", "Sí" if vehiculo.motor.encedido else "No")

    if vehiculo.conductor:
        print("="*50)
        print(" Información del Conductor Asignado:")
        print("="*50)
        print(" Nombre:", vehiculo.conductor.nombre)
        print(" Licencia:", vehiculo.conductor.licencia)
        print(" Identificación:", vehiculo.conductor.documento)
        
    else:
        print(" \n ❗ No hay conductor asignado a este vehículo.")

def main() -> None:
    print("🚗 Sistema de Gestión de Vehículos")
    print("="*50)
    print(" \n Inicializando motores y conductores...")
    
    
    motorMoto = Motor("gasolina", 150,True)
    motorCarro = Motor("electrico", 1800, True)
    motorCamion = Motor("gasolina", 5000, True)

    conductorMoto = Conductor("Juan Pablo","12343","A2",True,False,False)    
    conductorCarro = Conductor("Ana Perez","56789","B1",False,True,False)
    conductorCamion = Conductor("Luis Gomez","98765","C3",False,False,True)

    moto = Moto("AXD201","Yamaha","YZF R3","activo",2021,300,motorMoto)
    carro = Carro("XYZ789","Tesla","activo",motorCarro,2022,"Model S")
    camion = Camion("TRK456","Volvo","activo",motorCamion,2020,"Carga General")

    moto.asignarConductor(conductorMoto)
    carro.asignarConductor(conductorCarro)
    camion.asignarConductor(conductorCamion)

    gestion = GestionVehiculos()

    gestion.agregarVehiculo(moto)
    gestion.agregarVehiculo(carro)
    gestion.agregarVehiculo(camion)

    print("="*50)
    print("📋 VEHÍCULOS REGISTRADOS")
    print(gestion.listarVehiculos())
    print("="*50)
    
    print("="*50)
    print("🔍 DETALLE DE VEHÍCULOS\n")
    print("="*50)
    for placa in ["AXD201", "XYZ789", "TRK456"]:
        vehiculo = gestion.buscarPlaca(placa)
        mostrarInfoVehiculo(vehiculo)

    print("="*50)
    print("🏁 INICIANDO JORNADA DE VEHÍCULOS")
    print("="*50)

    for placa in ["AXD201", "XYZ789", "TRK456"]:
        vehiculo = gestion.buscarPlaca(placa)
        try:
            gestion.iniciarJornada(placa)
            print(f"✅ El conductor {vehiculo.conductor.nombre} inicia su jornada con su {type(vehiculo).__name__} marca {vehiculo.marca} con placa {placa}")
        except ValueError as e:
            print(f"❌ Error al iniciar jornada para {placa}: {e}")

if __name__ == "__main__":
    main()