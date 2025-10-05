class Cliente:
    __nome = str
    __cpf = str
    __limite = float
    __socio = None
    __eh_socio = bool
    
    def __init__(self, nome, cpf, limite):
        self.setNome(nome)
        self.setCpf(cpf)
        self.setLimite(limite)
        
    def setNome(self, nome):
        self.__nome = nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def setLimite(self, limite):
        self.__limite = limite

class Empresa:
    __nome = str
    __clientes = []
    
    def __init__(self, nome):
        self.setNome(nome)
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def inserir(self, cliente):
        self.__clientes.append(cliente)
    
    def listar(self):
        return self.__clientes
        