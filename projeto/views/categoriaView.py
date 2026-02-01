from dao_classes import CategoriaDAO
from models import Categoria
from utils import verifica_valor

class CategoriaView:
    @staticmethod
    def categoria_inserir(nome):
        for cat in CategoriaView.categoria_listar():
            if cat.getNome() == nome:
                raise ValueError("Categoria já existe") 
        categoria = Categoria(0, nome)
        CategoriaDAO.inserir(categoria)
        
    @staticmethod
    def categoria_listar():
        categorias = CategoriaDAO.listar()
        if len(categorias) == 0:
            raise ValueError("Não há categorias cadastradas")
        return categorias
        
    @staticmethod
    def categoria_atualizar(id, nome):
        if not(isinstance(id, int)):
            raise ValueError("O ID precisa ser um inteiro")
        id = int(id)
        antiga_categ = CategoriaDAO.busca_obj(id)
        nome = verifica_valor(antiga_categ.getNome(), nome, str)
        categoria = Categoria(id, nome)
        CategoriaDAO.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        for pro in CategoriaView.produto_listar():
            if pro.getCategoria() == id:
                raise ValueError("Essa categoria está em uso")
        categoria = Categoria(id, nome="")
        CategoriaDAO.excluir(categoria)