from .motor import Motor
from .vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, placa: str, marca: str, modelo: str, estado:bool,anio: int, cilindraje: int,motor:Motor) -> None:
        super().__init__(placa, marca, estado, motor)

        
        if isinstance(modelo, str) and modelo.strip():
            self._modelo = modelo.strip().title()
        else:
            raise ValueError("El modelo debe ser un texto no vacio")
        
        if isinstance(anio,int) and anio > 2000:
            self._anio = anio
        else:
            raise ValueError("El año de fabricación de la moto no puede ser anterior al 2000")

        
        if cilindraje >= 100 and cilindraje <= 350 and isinstance(cilindraje,int):
            self._cilindraje = cilindraje
        else:
            raise ValueError("Este cilindraje no esta permitido")
        
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
            raise ValueError("El año de la moto tiene que ser mayor a los 2000")

    @property
    def cilindraje(self) -> int:
        return self._cilindraje
    
    @cilindraje.setter
    def cilindraje(self, valor: int) -> None:
        if valor >= 100 and valor <= 350:
            self._cilindraje = valor
        else:
            raise ValueError("Este cilindraje no esta permitido")
        
    def iniciarJornada(self):
        if self.conductor is None:
            raise ValueError("La moto no tiene conductor asignado")

        if not self.conductor.tiene_casco:
            raise ValueError("El conductor debe portar casco antes de iniciar la jornada")

        self.encenderMotor()

    def finalizarJornada(self):
        self.apagarMotor()                
        return f"El conductor {self.conductor.nombre} de la moto con la placa {self.placa} finaliza su jornada laboral"
    
    def mover(self):
        return "La moto se dezplaza por la via"
    
    def mostrarInfo(self):
        return f"Moto: \n Marca:{self._marca} \n Placa:{self._placa} \n Modelo:{self._modelo} \n Año:{self._anio} \n Cilindraje:{self._cilindraje} \n Motor Tipo:{self._motor.tipo} \n Motor Cilindraje:{self._motor.cilindraje} \n Motor Velocidad:{self._motor.velocidad} \n Motor Encendido:{self._motor.encedido} \n Estado:{self._estado} \n Conductor:{self._conductor.nombre if self._conductor else 'No asignado'}"
    