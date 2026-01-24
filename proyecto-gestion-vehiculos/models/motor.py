
class Motor():
    def __init__(self,tipo:str,velocidad:int,encedido:bool):
        if tipo == "gasolina" or tipo == "electrico":
            self._tipo = tipo.upper()   
        else:
            raise ValueError("Este tipo de motor es invalido")          
        
        if velocidad > 0:
            self._velocidad = velocidad
        else:
            raise ValueError("La velocidad debe ser mayor a 0")
        
        if isinstance(encedido,bool):
            self._encedido = encedido
        else:
            raise ValueError("El estado del motor debe ser encedido o apagado")
        
    @property
    def tipo(self) -> str:
        return self._tipo
    
    @tipo.setter
    def tipo(self,valor:str) -> None:
        if valor == "gasolina" or valor == "electrico":
            self._tipo = valor.upper()
        else:
            raise ValueError("Este tipo de motor es invalido")
        
    @property
    def cilindraje(self) -> int:
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self,valor:int) -> None:
        if valor > 0:
            self._cilindraje = valor
        else:
            raise ValueError("El cilindraje debe ser mayor a 0")      

    @property
    def velocidad(self) -> int:
        return self._velocidad

    @velocidad.setter
    def velocidad(self,valor:int) -> None:
        if valor > 0:
            self._velocidad = valor
        else:
            raise ValueError("La velocidad debe ser mayor a 0")

    @property
    def encedido(self) -> bool:
        return self._encedido
    
    @encedido.setter
    def encedido(self,valor:bool) -> None:
        if isinstance(valor,bool):
            self._encedido = valor
        else:
            raise ValueError("El estado del motor debe ser encedido o apagado")
        
