
class Conductor:
    def __init__(self,nombre:str,documento:str,licencia:str,tieneCasco:bool,tecnoMecanica:bool,planillaCarga:bool)-> None:
        if isinstance(nombre,str) and nombre.strip():
            self._nombre = nombre.strip().title()
        else:
            raise ValueError("El nombre debe ser un texto no vacio")
        if isinstance(documento,str) and documento.strip():
            self._documento = documento
        else:
            raise ValueError("El documento debe ser un texto no vacio.")
        if isinstance(licencia,str) and licencia.strip():
            self._licencia = licencia.strip().upper()
        else:
            raise ValueError("La licencia debe ser un texto no vacio.")
        if isinstance(tieneCasco,bool):
            self._tieneCasco = tieneCasco       
        else:
            raise ValueError("El texto de tiene casco de su moto debe ser un valor de verdadero o falso")
        if isinstance(tecnoMecanica,bool):
            self._tecnoMecanica = tecnoMecanica
        else:
            raise ValueError("El texto de la técnico-mecánica vigente de su carro debe ser verdadero o falso") 
        if isinstance(planillaCarga,bool):
            self._planillaCarga = planillaCarga
        else:
            raise ValueError("El texto de la planilla de carga y maximo peso permitido debe ser verdadero o falso")        

                
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self,valor:str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._nombre = valor.strip().title()
        else:
            raise ValueError("El nombre debe ser un texto no vacio")

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._documento = valor
        else:
            raise ValueError("El documento debe ser un texto no vacio.")

    @property
    def licencia(self) -> str:
        return self._licencia

    @licencia.setter
    def licencia(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._licencia = valor.strip().upper()
        else:
            raise ValueError("La licencia debe ser un texto no vacio.")
        
    @property
    def tieneCasco(self)-> bool:
        return self._tieneCasco
    
    @tieneCasco.setter
    def tieneCasco(self,valor:bool)-> None:
        if isinstance(valor,bool):
            self._tieneCasco = valor       
        else:
            raise ValueError("El texto de tiene casco debe ser un valor de verdadero o falso")
        
    @property
    def tecnicoMecanica(self)-> bool:
        return self._tecnoMecanica
    
    @tecnicoMecanica.setter
    def tecnicoMecanica(self,valor:bool)-> None:
        if isinstance(valor,bool):
            self._tecnoMecanica = valor
        else:
            raise ValueError("El texto de tecno-mecanica vigente debe ser un valor verdadero o falso")
    
    @property
    def planillaCarga(self)-> bool:
        return self.planillaCarga
    
    @planillaCarga.setter
    def planillaCarga(self,valor:bool)-> None:
        if isinstance(valor,bool):
            self.planillaCarga = valor
        else:
            raise ValueError("El texto de planilla de carga y de peso maximo permitido debe ser un valor verdadero o falso")
    