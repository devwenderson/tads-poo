from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO

class View:
    # ===== CLIENTES =====
    @staticmethod
    def cliente_inserir(nome, email, telefone):
        cliente = Cliente(0, nome, email, telefone)
        ClienteDAO.inserir(cliente)
    
    @staticmethod
    def cliente_listar():
        clientes = ClienteDAO.listar()
        return clientes

    @staticmethod
    def cliente_atualizar(id, nome, email, telefone):
        try:
            cliente = Cliente(id, nome, email, telefone)
            ClienteDAO.atualizar(cliente)
            return True
        except:
            return False

    @staticmethod
    def cliente_excluir(id):
        View.listar_cliente()
        cliente = Cliente(id, nome="", email="", telef="")
        ClienteDAO.excluir(cliente)
    
    # ===== CATEGORIAS =====
    @staticmethod
    def categoria_inserir(nome):
        categoria = Categoria(0, nome)
        CategoriaDAO.inserir(categoria)
        
    @staticmethod
    def categoria_listar():
        categorias = CategoriaDAO.listar()
        return categorias
        
    @staticmethod
    def categoria_atualizar(id, nome):
        categoria = Categoria(id, nome)
        CategoriaDAO.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        categoria = Categoria(id, nome="")
        CategoriaDAO.excluir(categoria)
    
    # ===== PRODUTOS =====
    @staticmethod
    def produto_inserir(descricao, preco, estoque, categoria_id):
        produto = Produto(0, descricao, preco, estoque, categoria_id)
        ProdutoDAO.inserir(produto)
        
    @staticmethod
    def produto_listar():
        produtos = ProdutoDAO.listar()
        return produtos
        
    @staticmethod
    def atualizar_produto(id, descricao, preco, estoque, categoria_id):
        produto = Produto(id, descricao, preco, estoque, categoria_id)
        ProdutoDAO.atualizar(produto)

    @staticmethod
    def excluir_produto(id):
        produto = Produto(id, descricao="", preco=0.0, estoque=0, categoria=None)
        ProdutoDAO.excluir(produto)