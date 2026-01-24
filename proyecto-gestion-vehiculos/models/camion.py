from .vehiculo import Vehiculo
from .motor import Motor

class Camion(Vehiculo):
    def __init__(self, placa:str, marca:str, estado:bool, motor:Motor,anio:int,tipoCarga:str):
        super().__init__(placa, marca, estado, motor)
    
        if anio > 2000 and isinstance(anio,int):
            self._anio = anio
        else:
            raise ValueError("El año de fabricación del camión no puede ser anterior al 2000") 

        if isinstance(tipoCarga,str) and tipoCarga.strip():
            self._tipoCarga = tipoCarga
        else:
            raise ValueError("EL tipo de carga no puede estar vacío")            
            
    @property
    def anio(self) -> int:
        return self._anio
    
    @anio.setter
    def anio(self, valor: int) -> None:
        if valor > 2000:
            self._anio = valor
        else:
            raise ValueError("El año del camión tiene que ser mayor a los 2000")
        
    def iniciarJornada(self):
        if self.conductor == None:
            raise ValueError("El camion no tiene conductor")       
            
        if not self.conductor.tieneCasco:
            raise ValueError("El conductor debe tener una planilla de carga Y maximo peso permitido valida antes de comenzar la jornada")
        self.encenderMotor()    
        return f"El conductor {self.conductor.nombre} del camion con la placa {self.placa} inicia su jornada laboral"


    def finalizarJornada(self):
        self.apagarMotor()                
        return f"El conductor {self.conductor.nombre} del carro con la placa {self.placa} finaliza su jornada laboral"
    
    def mover(self):
        return "El camión se dezplaza por la via"
    
    def mostrarInfo(self):
        return f"Camión: \n Marca:{self._marca} \n Placa:{self._placa} \n Año:{self._anio} \n Tipo de Carga:{self._tipoCarga} \n Motor Tipo:{self._motor.tipo} \n Motor Velocidad:{self._motor.velocidad} \n Motor Encendido:{self._motor.encedido} \n Estado:{self._estado} \n Conductor:{self._conductor.nombre if self._conductor else 'No asignado'}"
