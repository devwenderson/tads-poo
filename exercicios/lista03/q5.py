def verifica_ano_bisexto(ano):
    resto_ano_400 = not(ano % 400)
    resto_ano_100 = not(ano % 100)
    resto_ano_4 = not(ano % 4)

    return resto_ano_100

class Data:
    __dia = int
    __mes = int
    __ano = int

    def __init__(self, dia, mes, ano):
        data = f"{dia}/{mes}/{ano}"
        self.setData(data)
    
    def __str__(self):
        return f"{self.getDia()}/{self.getMes()}/{self.getAno()}"

    def setDia(self, dia):
        self.__dia = dia
    
    def setMes(self, mes):
        if (mes > 12 or mes < 1): raise ValueError("Mês inválido")
        else:
            self.__mes = mes

    def setAno(self, ano):
        self.__ano = ano

    def setData(self, data):
        dia, mes, ano = map(int, data.split("/"))

        self.setDia(dia)
        self.setMes(mes)
        self.setAno(ano)

    def getDia(self):
        return self.__dia
    
    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

print(verifica_ano_bisexto(1900))