from models.interfazMovible import InterfazMovible
from .motor import Motor
from .conductor import Conductor
from abc import ABC,abstractmethod
    

class Vehiculo(InterfazMovible):
    def __init__(self,placa:str,marca:str,estado:bool,motor:Motor)-> None:
        if isinstance(placa,str) and placa.strip():
            self._placa = placa.strip().upper()
        else:
            raise ValueError("La placa debe ser válida")
        
        if isinstance(marca,str) and marca.strip():
            self._marca = marca.strip().title()
        else:
            raise ValueError("La marca debe ser valida")   
        
        valor = estado.lower()
        if valor in ("activo", "inactivo"):
            self._estado = valor
        else:
            raise ValueError("El estado debe ser 'Activo' o 'Inactivo'.")
        
        if isinstance(motor,Motor):
            self._motor = motor
        else:
            raise ValueError("El vehículo debe tener un motor válido.")
        
        self._conductor = None
        
    @property
    def placa(self) -> str:
        return self._placa
    
    @placa.setter
    def placa(self,valor:str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._placa = valor.strip().upper()
        else:
            raise ValueError("La placa debe ser válida")
    
    @property
    def marca(self) -> str:
        return self._marca
    
    @marca.setter
    def marca(self,valor:str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._marca = valor.strip().title()
        else:
            raise ValueError("La marca debe ser válida")   
    @property
    def motor(self) -> Motor:
        return self._motor
    
    @motor.setter
    def motor(self,valor:Motor) -> None:
        if isinstance(valor,Motor):
            self._motor = valor
        else:
            raise ValueError("El vehiculo debe tener un motor válido.")

    @property
    def estado(self) -> bool:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        valorNormal = valor.strip().lower()
        if valorNormal in ("activo", "inactivo"):
            self._estado = valorNormal
        else:
            raise ValueError("El estado debe ser 'Activo' o 'Inactivo'.")

    @property
    def conductor(self) -> Conductor:
        return self._conductor
    
    def asignarConductor(self,conductor:Conductor) -> None:
        if isinstance(conductor,Conductor):
            self._conductor = conductor
        else:
            raise ValueError("El vehiculo debe tener un conductor válido.")
        
    def eliminarConductor(self) -> None:
        self._conductor = None
        
    def encenderMotor(self) -> None:
        self._motor._encedido = True
        
    def apagarMotor(self) -> None:
        self._motor._encedido = False
        
    @abstractmethod
    def iniciarJornada(self):
        pass
        
    @abstractmethod
    def finalizarJornada(self):
        pass
    
        
    @abstractmethod
    def mostrarInfo(self):
        pass