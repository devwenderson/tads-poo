import json
from models import Cliente, Categoria, Produto, Venda, VendaItem
import os

class ClienteDAO:
    objetos = [Cliente]

    @classmethod
    def inserir(cls, obj):
        cls.abrir() 
        try:
            # ----- Escreve o ID automaticamente -----
            id = 0
            for aux in cls.objetos:
                if aux.id > id:
                    id = aux.id
            obj.setId(id + 1)
            # ----------------------------------------
            cls.objetos.append(obj)
            cls.salvar()
        except:
            # === SE O ARQUIVO NÃO EXISTIR ===
            obj.setId(1)
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
        path = os.path.dirname(__file__)
        with open(f"{path}/database/clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/clientes.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"])
                    cls.objetos.append(c)
        except:
            print("===== Arquivo não existe =====")

class CategoriaDAO:
    objetos = [Categoria]

    @classmethod
    def inserir(cls, obj):
        try:
            cls.abrir()
            id = 0
            for aux in cls.objetos:
                if aux.id > id:
                    id = aux.id
            obj.id = id + 1
            cls.objetos.append(obj)
            cls.salvar()
        except:
            obj.setId(1)
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
        path = os.path.dirname(__file__)
        with open(f"{path}/database/categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/categorias.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = Categoria(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass

class ProdutoDAO:
    objetos = [Produto]

    @classmethod
    def inserir(cls, obj):
        try:
            cls.abrir()
            id = 0
            for aux in cls.objetos:
                if aux.id > id:
                    id = aux.id
            obj.id = id + 1
            cls.objetos.append(obj)
            cls.salvar()
        except:
            obj.setId(1)
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
        path = os.path.dirname(__file__)
        with open(f"{path}/database/produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        path = os.path.dirname(__file__)
        with open(f"{path}/database/produtos.json", mode="r") as arquivo:
            list_dict = json.load(arquivo)
            for dic in list_dict:
                p = Produto(
                    dic["id"], 
                    dic["descricao"], 
                    dic["preco"], 
                    dic["estoque"], 
                    dic["categoria"]
                )
                cls.objetos.append(p)

class VendaDAO:
    objetos = [Venda]

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
        path = os.path.dirname(__file__)
        with open(f"{path}/database/vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        path = os.path.dirname(__file__)
        with open(f"{path}/database/vendas.json", mode="r") as arquivo:
            list_dict = json.load(arquivo)
            for dic in list_dict:
                c = Venda(
                    dic["id"],
                    dic["data"],
                    dic["carrinho"],
                    dic["total"],
                    dic["cliente"]
                )
                cls.objetos.append(c)

class VendaItemDAO:
    objetos = [VendaItem]

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
        path = os.path.dirname(__file__)
        with open(f"{path}/database/venda-tens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars, indent=4)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        path = os.path.dirname(__file__)
        with open(f"{path}/database/venda-itens.json", mode="r") as arquivo:
            list_dict = json.load(arquivo)
            for dic in list_dict:
                c = VendaItem(
                    dic["id"],
                    dic["qtd"],
                    dic["preco"],
                    dic["venda"],
                    dic["produto"]
                )
                cls.objetos.append(c)