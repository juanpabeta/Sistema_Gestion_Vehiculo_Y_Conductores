from .vehiculo import Vehiculo
from .motor import Motor

class Carro(Vehiculo):
    def __init__(self, placa:str, marca:str, estado:bool, motor:Motor,anio:int,modelo:str):
        super().__init__(placa, marca, estado, motor)
        
        if isinstance(modelo, str) and modelo.strip():
            self._modelo = modelo.strip().title()
        else:
            raise ValueError("El modelo debe ser un texto no vacio")        
        if anio > 2000 and isinstance(anio,int):
            self._anio = anio
        else:
            raise ValueError("El año de fabricación del carro no puede ser anterior al 2000")

    @property
    def modelo(self) -> str:
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._modelo = valor.strip().title()
        else:
            raise ValueError("El modelo debe ser un texto no vacio")
        
    @property
    def anio(self) -> int:
        return self._anio
    
    @anio.setter
    def anio(self, valor: int) -> None:
        if valor > 2000:
            self._anio = valor
        else:
            raise ValueError("El año del carro tiene que ser mayor a los 2000")
        
        
    def iniciarJornada(self):        
        if self.conductor == None:
            raise ValueError("El carro no tiene conductor")
            
        if not self.conductor.tecnicoMecanica:
            raise ValueError("El conductor debe tener una revisión de técnico-mecánica valida antes de comenzar la jornada")
        self.encenderMotor()    
        return f"El conductor {self.conductor.nombre} del carro con la placa {self.placa} inicia su jornada laboral"

    def finalizarJornada(self):
        self.apagarMotor()                
        return f"El conductor {self.conductor.nombre} del carro con la placa {self.placa} finaliza su jornada laboral"
    
    def mover(self):
        return "El carro se dezplaza por la via"

    def mostrarInfo(self):
        return f"Carro: \n Marca:{self._marca} \n Placa:{self._placa} \n Modelo:{self._modelo} \n Año:{self._anio} \n Motor Tipo:{self._motor.tipo} \n Motor Velocidad:{self._motor.velocidad} \n Motor Encendido:{self._motor.encedido} \n Estado:{self._estado} \n Conductor:{self._conductor.nombre if self._conductor else 'No asignado'}"