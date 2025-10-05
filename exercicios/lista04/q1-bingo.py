import random
class Bingo:
    __numBolas = int
    __bolas = []
    __bolasSorteadas = []

    def __init__(self, numBolas):
        self.setNumBolas(numBolas)
        self.setBolas(numBolas)
    
    def setNumBolas(self, numBolas):
        self.__numBolas = numBolas
    
    def setBolas(self, numBolas):
        for i in range(numBolas):
            self.__bolas.append(i+1)
    
    def getNumBolas(self):
        return self.__numBolas
    
    def getBolas(self):
        return self.__bolas

    def sorteadas(self):
        return self.__bolasSorteadas

    def proximo(self):
        bolas = self.getBolas()

        if (len(bolas) == 0): return bolas

        sor = random.choice(bolas)
        bolas.remove(sor)
        self.__bolasSorteadas.append(sor)

""" Bingo funcionando """

bingo = Bingo(10)
numBolas = len(bingo.getBolas())
i = 0
while (numBolas != 0):
    bingo.proximo()
    sorteadas = bingo.sorteadas()
    print(f"Bola sorteada: {sorteadas[i]}")
    i += 1
    numBolas -= 1
