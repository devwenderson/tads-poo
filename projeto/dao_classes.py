import json
from models import Cliente, Categoria, Produto, Venda, VendaItem, Endereco, Fornecedor, ProdutoEntrega, Entrega
import os
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self):
        self.objetos = []

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
    @abstractmethod
    def get_classe(cls):
        pass

    @classmethod
    @abstractmethod
    def get_arquivo(cls):
        pass

    @classmethod
    def salvar(cls):
        path = os.path.dirname(__file__)
        with open(f"{path}/database/{cls.get_arquivo()}", mode="w") as arquivo:
            json.dump(
                cls.objetos,
                arquivo,
                default=cls.get_classe().to_json,
                indent=4
            )

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []
            path = os.path.dirname(__file__)
            with open(f"{path}/database/{cls.get_arquivo()}", mode="r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    obj = cls.get_classe().from_json(dic)
                    cls.objetos.append(obj)
        except Exception as e:
            print(f"ERRO AO ABRIR: {e}")

class ClienteDAO(DAO):   
    @classmethod
    def get_classe(cls):
        return Cliente

    @classmethod
    def get_arquivo(cls):
        return "clientes.json"

class CategoriaDAO(DAO):  
    @classmethod
    def get_classe(cls):
        return Categoria

    @classmethod
    def get_arquivo(cls):
        return "categorias.json"

        
class ProdutoDAO(DAO):
    @classmethod
    def get_classe(cls):
        return Produto

    @classmethod
    def get_arquivo(cls):
        return "produtos.json"

class VendaDAO(DAO):
    @classmethod
    def listar(cls, is_carrinho=True, carrinho_only=False, cliente_id=None):
        """
        is_carrinho: True -> Retorna carrinho
        is_carrinho: False -> Retorna vendas
        cliente_id: None -> Retorna todas as vendas
        cliente_id: int -> Retorna vendas de um único cliente
        carrinho_only: True -> Retorna apenas carrrinho
        carrinho_only: False -> Retorna tudo
        """
        cls.abrir()
        if (carrinho_only):
            return [i for i in cls.objetos if i.getCliente() == cliente_id and i.getCarrinho()]
        
        if (is_carrinho):
            if cliente_id != None:
                return [i for i in cls.objetos if i.getCliente() == cliente_id]
            return cls.objetos
        else:
            if (cliente_id != None):
                return [i for i in cls.objetos if i.getCliente() == cliente_id]
            else:  
                return [i for i in cls.objetos if i.getCarrinho() is not True]
    
    @classmethod
    def get_classe(cls):
        return Venda

    @classmethod
    def get_arquivo(cls):
        return "vendas.json"
        
class VendaItemDAO(DAO):
    @classmethod
    def listar(cls, venda=None):
        cls.abrir()
        if (venda != None):
            return [i for i in cls.objetos if venda.getId() == i.getVenda()]
        else:
            return cls.objetos
    
    @classmethod
    def get_classe(cls):
        return VendaItem

    @classmethod
    def get_arquivo(cls):
        return "venda-itens.json"

class EnderecoDAO(DAO):
    @classmethod
    def get_classe(cls):
        return Endereco

    @classmethod
    def get_arquivo(cls):
        return "enderecos.json"
    
class FornecedorDAO(DAO):
    @classmethod
    def get_classe(cls):
        return Fornecedor

    @classmethod
    def get_arquivo(cls):
        return "fornecedores.json"
    
class EntregaDAO(DAO):
    @classmethod
    def get_classe(cls):
        return Entrega

    @classmethod
    def get_arquivo(cls):
        return "entregas.json"
    
class ProdutoEntregaDAO(DAO):
    @classmethod
    def get_classe(cls):
        return ProdutoEntrega

    @classmethod
    def get_arquivo(cls):
        return "produto-entregas.json"