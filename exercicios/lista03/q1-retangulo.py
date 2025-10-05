class Retangulo:
    __base = 0
    __altura = 0

    def __init__(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)
    
    def __str__(self):
        return f"Base: {self.getBase()}\nAltura: {self.getAltura()}\nÁrea: {self.calcArea()}\nDiagonal: {self.calcDiagonal()}"

    def setBase(self, base):
        self.__base = base
    
    def setAltura(self, altura):
        self.__altura = altura
    
    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self.__altura
    
    def calcArea(self):
        return self.__base * self.__altura
    
    def calcDiagonal(self):
        return ((self.__base ** 2) + (self.__altura ** 2)) ** 0.5

ret1 = Retangulo(8, 6)
print(ret1)

    
