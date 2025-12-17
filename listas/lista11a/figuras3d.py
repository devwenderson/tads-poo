from abc import ABC, abstractmethod
import math

class Figura3D(ABC):
    @abstractmethod
    def getVolume():
        pass

class Esfera(Figura3D):
    def __init__(self, raio):
        self.__raio = raio
    
    def __str__(self):
        return f"Volume: {self.getVolume():.02f} "

    def getVolume(self):
        return ((4/3)*math.pi) * (self.__raio**3)

class Cubo(Figura3D):
    def __init__(self, lado):
        self.__lado = lado

    def __str__(self):
        return f"Volume: {self.getVolume()}"

    def getVolume(self):
        return self.__lado**3

e1 = Esfera(15)
print(e1)

c1 = Cubo(10)
print(c1)