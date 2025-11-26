import math
import pandas as pd
import streamlit as st

class Equacao2Grau:
    def __init__(self, a, b, c):
        self.setA(a)
        self.setB(b)
        self.setC(c)
        if a == 0: raise ValueError("Não é uma equação do 2° grau")
    
    def __str__(self):
        texto = ""
        texto += f"Coeficientes: a={self.__a}, b={self.__b}, c={self.__c}\n"
        texto += f"Delta: {self.delta()}\n"
        texto += f"X1 = {self.x1()} | X2 = {self.x2()}\n"
        texto += f"Ponto de inflexão: {self.ponto_inflexao()}"
        return texto
    
    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b

    def setC(self, c):
        self.__c = c
    
    def delta(self):
        a = self.__a
        b = self.__b
        c = self.__c
        return ((b*b) - (4 * (a * c)))
    
    def x1(self):
        delta = self.delta()
        a = self.__a
        b = self.__b
        if delta >= 0: return (-b + math.sqrt(delta)) / (2 * a)
        else: f"{-b / (2 * a)} + {math.sqrt(-delta) / (2 * a)}"
      
    def x2(self):
        delta = self.delta()
        a = self.__a
        b = self.__b
        if delta >= 0: return (-b - math.sqrt(delta)) / (2 * a)
        else: f"{-b / (2 * a)} + {math.sqrt(-delta) / (2 * a)}"
    
    def ponto_inflexao(self):
        return -self.__b / (2*self.__a)
    
    def y(self, x):
        return (self.__a*(x*x)) + (self.__b * x) + (self.__c)

f = Equacao2Grau(1, -5, 6)
print(f)
p = f.ponto_inflexao()
xmin = p - 10
xmax = p + 10
npontos = 50
dist = (xmax - xmin) / (npontos - 1)
x = xmin
px = []
py = []
while x <= xmax:
    px.append(x)
    py.append(f.y(x))
    #print(x, y)
    x += dist

df = pd.DataFrame({"x": px, "y": py})
st.line_chart(df, x="x", y="y")