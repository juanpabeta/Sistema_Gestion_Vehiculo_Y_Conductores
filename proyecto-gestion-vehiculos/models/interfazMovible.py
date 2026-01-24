from abc import ABC,abstractmethod

class InterfazMovible(ABC):    
    
    @abstractmethod
    def mover(self):
        pass   