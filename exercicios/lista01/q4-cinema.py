class Ingresso:
    dia = ""
    horario = None
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario
    
    def inteira(self):
        if self.dia in ["seg", "ter", "qui"]:
            valor = 16
            if self.horario == 0 or self.horario >= 17:
                return valor * 1.5
            return valor
        
        elif self.dia == "qua":
            return 8
        
        elif self.dia in ["sex", "sab", "dom"]:
            valor = 20
            if self.horario == 0 or self.horario >= 17:
                return valor * 1.5
            return valor
    
    def meia(self):
        if self.dia == "qua":
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
        ingr = Ingresso(dia, horario) 
        preco_inteira = ingr.inteira()
        preco_meia = ingr.meia()
        print(f"Preço da inteira: R${preco_inteira:0.2f}")
        print(f"Preço da meia: R${preco_meia:0.2f}")

UI.main()