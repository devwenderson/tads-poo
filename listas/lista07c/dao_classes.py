import json
from models import Cliente, Categoria, Produto, Venda, VendaItem
import os

class ClienteDAO:
    objetos = [Cliente]

    @classmethod
    def inserir(cls, obj):
        cls.abrir() 
        id = 0
        for aux in cls.objetos:
            if aux.getId() > id: id = aux.getId()
        obj.setId(id + 1)
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
            json.dump(cls.objetos, arquivo, default=Cliente.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/clientes.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = Cliente.from_json(dic)
                    cls.objetos.append(c)
            return True
        except:
            return False

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
            json.dump(cls.objetos, arquivo, default=Categoria.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/categorias.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = Categoria.from_json(dic)
                    cls.objetos.append(c)
            return True
        except:
            return False

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
            json.dump(cls.objetos, arquivo, default=Produto.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/produtos.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    p = Produto.from_json(dic)
                    cls.objetos.append(p)
            return True
        except:
            return False

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
    def listar(cls, is_carrinho=True, cliente_id=None):
        """
        is_carrinho: True -> Retorna carrinho
        is_carrinho: False -> Retorna vendas
        cliente_id: None -> Retorna todas as vendas
        cliente_id: int -> Retorna vendas de um único cliente
        """
        cls.abrir()
        if (is_carrinho):
            if cliente_id != None:
                return [i for i in cls.objetos if i.getCliente() == cliente_id]
            return cls.objetos
        else:
            if (cliente_id != None):
                return [i for i in cls.objetos if i.getCliente() == cliente_id]
            else:  
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
            json.dump(cls.objetos, arquivo, default=Venda.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/vendas.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = Venda.from_json(dic)
                    cls.objetos.append(c)
            return True
        except:
            return False
        
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
    def listar(cls, venda=None):
        cls.abrir()
        if (venda != None):
            return [i for i in cls.objetos if venda.getId() == i.getVenda()]
        else:
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
        with open(f"{path}/database/venda-itens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=VendaItem.to_json, indent=4)
    
    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/venda-itens.json", mode="r") as arquivo:
                list_dict = json.load(arquivo)
                for dic in list_dict:
                    c = VendaItem.from_json(dic)
                    cls.objetos.append(c)
            return True
        except:
            return False