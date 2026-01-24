from models.vehiculo import Vehiculo


class GestionVehiculos:

    def __init__(self):
        self._vehiculos = []

    def agregarVehiculo(self, vehiculo: Vehiculo):
        if not isinstance(vehiculo, Vehiculo):
            raise ValueError("Solo se pueden agregar vehículos válidos")

        if self.buscarPlaca(vehiculo.placa) is not None:
            raise ValueError("Ya existe un vehículo con esa placa")

        self._vehiculos.append(vehiculo)

        
    def listarVehiculos(self):
        if not self._vehiculos:
            return "No hay vehículos registrados"

        resultado = ""
        for vehiculo in self._vehiculos:
            resultado += f" {type(vehiculo).__name__} - {vehiculo.placa} - {vehiculo.marca}\n"

        return resultado

    def buscarPlaca(self, placa: str):
        for vehiculo in self._vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None


    def iniciarJornada(self, placa: str):
        vehiculo = self.buscarPlaca(placa)

        if vehiculo is None:
            raise ValueError("Vehículo no encontrado")
    
        
    
    def finalizarJornada(self, placa: str):
        vehiculo = self.buscarPlaca(placa)

        if vehiculo is None:
            raise ValueError("Vehículo no encontrado")

      
