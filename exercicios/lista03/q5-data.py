"""
400 or (4 xor 100)

1   or  (1 and not(1)) = 1

0   or  (1 and not(1)) = 0

0   or  (1 and not(0)) = 1

"""
def dias_mes(mes):
    n_mes = mes + (mes//8)
    dias_do_mes = 30 + (n_mes & 1)
    return dias_do_mes

class Data:
    __dia = 0
    __mes = 0
    __ano = 0

    def __init__(self, dia, mes, ano):
        data = f"{dia}/{mes}/{ano}"
        self.setData(data)
    
    def __str__(self):
        eh_bissexto = "Sim" if self.bissexto() else "Não"
        return f"{self.getDia():02d}/{self.getMes():02d}/{self.getAno():04d}\nÉ bissexto: {eh_bissexto}"

    def setData(self, data):
        dia, mes, ano = map(int, data.split("/"))

        # A ordem dos métodos é importante
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)

    def setDia(self, dia):
        mes = self.getMes()
        n_mes = mes + (mes//8)
        dias_do_mes = 30 + (n_mes & 1)

        eh_bissexto = self.bissexto()

        if (dia < 1): raise ValueError("Dia inválido")

        if (mes != 2):
            if (dia > dias_do_mes): raise ValueError("Dia inválido")
        else:
            if (eh_bissexto and dia > 29): raise ValueError("Dia inválido")
            elif (not(eh_bissexto) and dia > 28): raise ValueError("Dia inválido")


        self.__dia = dia
    
    def setMes(self, mes):
        if (mes > 12 or mes < 1): raise ValueError("Mês inválido")
        self.__mes = mes

    def setAno(self, ano):
        if (ano < 0): raise ValueError("Ano inválido")
        self.__ano = ano

    def getDia(self):
        return self.__dia
    
    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano
    
    def bissexto(self):
        ano = self.getAno()
        div_400 = not(ano % 400)
        div_100 = not(ano % 100)
        div_4 = not(ano % 4)

        eh_bissexto = div_400 or (div_4 and not(div_100))

        return eh_bissexto

data = Data(1, 2, 1004)
print(data)
