from dao_classes import ProdutoDAO
from models import Produto
from utils import verifica_valor

class ProdutoView:
    @staticmethod
    def produto_inserir(descricao, preco, estoque, categoria_id):

        for prod in ProdutoView.produto_listar():
            if descricao == prod.getDescricao():
                raise ValueError("Produto já existe")

        produto = Produto(0, descricao, preco, estoque, categoria_id)
        ProdutoDAO.inserir(produto)
        
    @staticmethod
    def produto_listar():
        produtos = ProdutoDAO.listar()
        if len(produtos) == 0:
            raise ValueError("Não há produtos cadastrados")
        return produtos
        
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, categoria_id):
        if not(isinstance(id, int)):
            raise ValueError("O ID precisa ser um inteiro")
        
        id = int(id)
        antigo_produto = ProdutoDAO.busca_obj(id)

        descricao = verifica_valor(antigo_produto.getDescricao(), descricao, str)
        preco = verifica_valor(antigo_produto.getPreco(), preco, float)
        estoque = verifica_valor(antigo_produto.getEstoque(), estoque, int)
        categoria_id = verifica_valor(antigo_produto.getCategoria(), categoria_id, int)

        produto = Produto(id, descricao, preco, estoque, categoria_id)
        ProdutoDAO.atualizar(produto)

    @staticmethod
    def produto_excluir(id):
        produto = Produto(id, descricao="", preco=0.0, estoque=0, categoria_id=1)
        ProdutoDAO.excluir(produto)
    
    @staticmethod
    def produto_reajustar(percentual):
        produtos = ProdutoView.produto_listar()
        for p in produtos:
            valor_reajustado = p.getPreco() * (1 + (percentual/100))
            ProdutoView.produto_atualizar(p.getId(), p.getDescricao(), valor_reajustado, p.getEstoque(), p.getCategoria())
     