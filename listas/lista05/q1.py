from datetime import datetime

class Paciente:
    __nome = str
    __cpf = str
    __telefone = str
    __nascimento = None

    def __init__(self, nome, cpf, telefone, nascimento):
        self.setNome(nome)
        self.setCpf(cpf)
        self.setTelefone(telefone)
        self.setNascimento(nascimento)
    
    # Métodos set
    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setNascimento(self, nascimento):
        n = datetime.strptime(nascimento, "%d/%m/%Y")
        self.__nascimento = n.date()

    # Métodos get
    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getTelefone(self):
        return self.__telefone

    def calcula_idade(self):
        tempo_atual = datetime.now().date()
        # tempo_atual = datetime(2025, 10, 19).date()
        nasci = self.__nascimento

        ano_atual = tempo_atual.year
        mes_atual = tempo_atual.month
        dia_atual = tempo_atual.day

        ano_nasci = nasci.year
        mes_nasci = nasci.month
        dia_nasci = nasci.day

        anos_idade = ano_atual - ano_nasci
        meses_idade = mes_atual - mes_nasci
        dias_idade = dia_atual - dia_nasci

        if ((meses_idade < 0) or (meses_idade == 0 and dias_idade < 0)):
            anos_idade -= 1
            meses_idade += 12
        
        if (dias_idade < 0):
            n_mes = mes_atual + (mes_atual//8)
            dias_do_mes = 30 + (n_mes & 1)
            meses_idade -= 1
            dias_idade += dias_do_mes

        idade = f"{anos_idade} anos e {meses_idade} meses e {dias_idade} dias"
        return idade

wenderson = Paciente("Wenderson", "123.456.789.10", "(84) 91234-5678", "19/09/2005")
print(wenderson.calcula_idade())
