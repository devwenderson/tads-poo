class Frete:
    def __init__(self, distancia, peso):
        self.__distancia = distancia
        self.__peso = peso

    def __str__(self):
        return f"Frete normal: Distância: {self.__distancia} - Peso: {self.__peso} - Valor: R$ {self.valorFrete():.02f}"

    def getDistancia(self):
        return self.__distancia

    def getPeso(self):
        return self.__peso

    def valorFrete(self):
        return ((self.__distancia * self.__peso) * 0.01)
    
class FreteExpresso(Frete):
    def __init__(self, d, p, s):
        super().__init__(d, p)
        self.__seguro = s

    def __str__(self):
        return f"Frete Expresso: Distância: {super().getDistancia()} - Peso: {super().getPeso()} - Preço: R$ {self.valorFrete()}"

    def valorFrete(self):
        return (super().valorFrete() *2) + (self.__seguro / 100)

f1 = FreteExpresso(100, 500, 100)
print(f1)

f2 = Frete(100, 500)
print(f2)