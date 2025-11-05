from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO

class View:
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