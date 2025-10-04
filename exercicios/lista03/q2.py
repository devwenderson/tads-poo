class Frete:
    __distancia = float # Em Km
    __peso = float # Em Kg

    def __init__(self, distancia, peso):
        self.setDistancia(distancia)
        self.setPeso(peso)
    
    def __str__(self):
        return f"Distancia: {self.getDistancia()}Km\nPeso: {self.getPeso()}Kg\nPreço: R$ {self.calcFrete():0.2f}"

    def setDistancia(self, distancia):
        self.__distancia = distancia
    
    def setPeso(self, peso):
        self.__peso = peso
    
    def getDistancia(self):
        return self.__distancia
    
    def getPeso(self):
        return self.__peso
    
    def calcFrete(self):
        preco_por_kg = self.getPeso() * 0.01 # 1 Cent por Kg
        preco_por_km = preco_por_kg * self.getDistancia() # Cent x Kg x Distancia
        return preco_por_km

frete1 = Frete(400, 50)
print(frete1)