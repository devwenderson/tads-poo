from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO
from utils import verifica_valor

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
        id = int(id)
        antigo_cli = ClienteDAO.busca_obj(id)

        nome = verifica_valor(antigo_cli.getNome(), nome, str)
        email = verifica_valor(antigo_cli.getEmail(), email, str)
        telefone = verifica_valor(antigo_cli.getTelefone(), telefone, str)

        cliente = Cliente(id, nome, email, telefone)
        ClienteDAO.atualizar(cliente)


    @staticmethod
    def cliente_excluir(id):
        id = int(id)
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
        id = int(id)

        antiga_categ = CategoriaDAO.busca_obj(id)

        nome = verifica_valor(antiga_categ.getNome(), nome, str)

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
    def produto_atualizar(id, descricao, preco, estoque, categoria_id):
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
        produtos = View.produto_listar()
        for p in produtos:
            valor_reajustado = p.getPreco() * (1 + (percentual/100))
            View.produto_atualizar(p.getId(), p.getDescricao(), valor_reajustado, p.getEstoque(), p.getCategoria())

