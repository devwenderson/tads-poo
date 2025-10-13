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
    
    def __str__(self):
        if (self.__socio == None):
            msg = f"Nome: {self.getNome()}\n"
            msg += f"Limite individual: {self.getLimite()}\n"
            return msg
        else:
            msg = f"Nome: {self.getNome()}\n"
            msg += f"Limite individual: {self.getLimite()}\n"
            msg += f"Sócio: {self.__socio.__nome}\n"
            msg += f"Limite da sociedade: {self.getLimiteSociedade()}\n"
            return msg
        
    def setNome(self, nome):
        self.__nome = nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def setLimite(self, limite):
        self.__limite = limite
    
    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getLimite(self):
        return self.__limite

    def getLimiteSociedade(self):
        if (self.__socio == None): return self.__limite
        else: return self.__limite + self.__socio.__limite
    
    def setSocio(self, socio):
        if (self.__socio):
            self.__socio = None
            self.__socio.__socio = None
        self.__socio = socio
        socio.__socio = self


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

cliente1 = Cliente("Alberto", "1234", 1000.0)
cliente2 = Cliente("Jorge", "5678", 1200.0)
cliente3 = Cliente("Maria", "5678", 1300.0)

print("======= Antes do socio =======")
print(cliente1)
print(cliente2)
print(cliente3)
cliente1.setSocio(cliente2)
cliente3.setSocio(cliente1)

print("======= Depois do socio =======")
print(cliente1)
print(cliente2)
print(cliente3)

cliente3.setSocio(cliente2)
print("======= Maria mudou de sócio =======")
print(cliente1)
print(cliente2)
print(cliente3)