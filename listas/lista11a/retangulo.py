import math

class Retangulo:
    def __init__(self, b, h):
        self.__b = b
        self.__h = h

    def __str__(self):
        return f"Altura={self.__h} | Base={self.__b} | Area={self.calcArea()} | Diagonal={self.calcDiagonal():.02f}"

    def getBase(self):
        return self.__b

    def getAltura(self):
        return self.__h

    def calcArea(self):
        return self.__b * self.__h

    def calcDiagonal(self):
        return math.sqrt((self.__b**2) + (self.__h**2))

class Quadrado(Retangulo):
    def __init__(self, b, h):
        super().__init__(b, h)
    
    def __str__(self):
        return f"Quadrado: " + super().__str__()

q1 = Quadrado(5, 5)
print(q1)