class Conversor:
    __numero = int

    def __init__(self, num):
        self.setNum(num)
    
    def __str__(self):
        return f"Decimal: {self.getNum()}\nBinário: {self.binario()}"

    def setNum(self, num):
        self.__numero = num
    
    def getNum(self):
        return self.__numero
    
    def binario(self):
        quo = self.getNum()
        binario = ""
        while (quo != 0):
            resto = quo % 2
            binario = binario + str(resto)
            quo = quo // 2

        reversed_binario = ""
        for i in range(len(binario)):
            reversed_binario = binario[i] + reversed_binario

        return reversed_binario

num = Conversor(182738)
print(num)