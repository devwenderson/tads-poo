import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id:
                id = aux.id
        obj.id = id + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def busca_obj(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.busca_obj(obj.id)
        # Substitui o objeto antigo pelo novo
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.busca_obj(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
        cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("./aulas/aula_13/clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("./aulas/aula_13/clientes.json", mode="r") as arquivo:
            list_dict = json.load(arquivo)
            for dic in list_dict:
                c = Cliente(dic["id"], dic["nome"])
                cls.objetos.append(c)


class UI:
    def menu():
        print("1-Inserir\n2-Listar\n3-Atualizar\n4-Excluir\n5-Fechar")
        return int(input("Informe uma opção: "))
    
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1:
                UI.inserir()
            if op == 2:
                UI.listar()
            if op == 3:
                UI.atualizar()
            if op == 4:
                UI.excluir()

    def inserir():
        cli_nome = input("Nome: ")
        cliente = Cliente(0, cli_nome)
        ClienteDAO().inserir(cliente)

    def listar():
        objetos = ClienteDAO().listar()
        for obj in objetos:
            print(f"ID: {obj.id} - Nome: {obj.nome}")

    def atualizar():
        UI.listar()
        id = int(input("ID a ser atualizado: "))
        nome = input("Novo nome: ")
        c = Cliente(id, nome)
        ClienteDAO.atualizar(c)

    def excluir():
        UI.listar()
        id = int(input("ID a ser excluido: "))
        nome = ""
        c = Cliente(id, nome)
        ClienteDAO.excluir(c)

UI.main()