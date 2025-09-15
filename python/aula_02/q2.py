'''
1 trimestre: jan, fev, mar
2 tri: abr, mai, jun
3 tri: jul, ago, set
4 tri: out, nov, dez
'''
n = int(input())

trimestre = ""
mes = ""

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

for i in range(len(meses)):
    if i == (n - 1):
        mes = meses[i]
        if n >= 1 and n <= 3:
            trimestre = "primeiro" 
        elif n >= 4 and n <= 6:
            trimestre = "segundo" 
        elif n >= 7 and n <= 9:
            trimestre = "terceiro" 
        elif n >= 10 and n <= 12:
            trimestre = "quarto" 

print(f"O mês de {mes} é do {trimestre} trimestre")