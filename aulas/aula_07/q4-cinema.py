"""
Aula 07 - Encapsulamento
"""

class Ingresso:
    __dia = ""
    __horario = None
    def __init__(self):
        self.__dia = str
        self.__horario = int

    # Encapsulamento
    def get_dia(self):
        return self.__dia
    
    def get_horario(self):
        return self.__horario
    
    def set_dia(self, dia):
        if (dia in ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]):
            self.__dia = dia
        else:
            raise ValueError("Dia inválido")

    def set_horario(self, horario):
        if (horario >= 0 and horario <= 23):
            self.__horario = horario
        else:
            raise ValueError("Hora Inválida")
    # Fim encapsulamento

    def inteira(self):
        dia = self.__dia
        horario = self.__horario
        if dia in ["seg", "ter", "qui"]:
            valor = 16
            if horario == 0 or horario >= 17:
                return valor * 1.5
            return valor
        
        elif dia == "qua":
            return 8
        
        elif dia in ["sex", "sab", "dom"]:
            valor = 20
            if horario == 0 or horario >= 17:
                return valor * 1.5
            return valor
    
    def meia(self):
        dia = self.__dia
        if dia == "qua":
            return 8
        return self.inteira()/2


class UI:
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1:
                UI.ingresso()
        print("Saindo...")
        
    def menu():
        opcoes = ["1 - Ingressos", "2 - Sair"]

        for i in opcoes:
            print(i)

        op = int(input("Escolha uma opção: "))
        return op
    
    def ingresso():
        dia = input("Informe o dia: ")
        horario = int(input("Informe o horário: "))
        ingr = Ingresso()
        ingr.set_dia(dia)
        ingr.set_horario(horario) 
        preco_inteira = ingr.inteira()
        preco_meia = ingr.meia()
        print(f"Preço da inteira: R${preco_inteira:0.2f}")
        print(f"Preço da meia: R${preco_meia:0.2f}")

UI.main()

    