class EquacaoIIGrau:
    __a = int
    __b = int
    __c = int

    def __init__(self, a, b, c):
        self.setA(a)
        self.setB(b)
        self.setC(c)
    
    def __str__(self):
        if (not(self.temRaizesReais())): return "Não há raízes reais"

        return f"Raiz 1: {self.raiz_1()}\nRaiz 2: {self.raiz_2()}"

    def setA(self, a):
        self.__a = a

    def getA(self):
        return self.__a

    def setB(self, b):
        self.__b = b

    def getB(self):
        return self.__b

    def setC(self, c):
        self.__c = c

    def getC(self):
        return self.__c

    def delta(self):
        a = self.getA()
        b = self.getB()
        c = self.getC()
        d = (b**2) - (4*a*c)

        return d

    def raiz_1(self):
        a = self.getA()
        b = 0 - self.getB()
        c = self.getC()
        d = self.delta()

        r1 = (b + (d**0.5)) / (2*a)

        return r1

    def raiz_2(self):
        a = self.getA()
        b = 0 - self.getB()
        c = self.getC()
        d = self.delta()

        r2 = (b - (d**0.5)) / (2*a)

        return r2

    def temRaizesReais(self):
        if (self.delta() < 0): return False
        else: return True

equa = EquacaoIIGrau(2, 1, 0)

print(equa)