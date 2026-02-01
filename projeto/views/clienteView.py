from dao_classes import ClienteDAO
from models import Cliente
from utils import verifica_valor

class ClienteView:
    @staticmethod
    def cliente_inserir(nome, email, senha, telefone):
        
        for cli in ClienteView.cliente_listar():
            if email == cli.getEmail():
                raise ValueError("Cliente já cadastrado")
            
        cliente = Cliente(0, nome, email, senha, telefone)
        ClienteDAO.inserir(cliente)
    
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, telefone, senha):
        if not(isinstance(id, int)):
            raise ValueError("O ID precisa ser um inteiro")
        
        id = int(id)
        antigo_cli = ClienteDAO.busca_obj(id)

        nome = verifica_valor(antigo_cli.getNome(), nome, str)
        email = verifica_valor(antigo_cli.getEmail(), email, str)
        telefone = verifica_valor(antigo_cli.getTelefone(), telefone, str)
        senha = verifica_valor(antigo_cli.getSenha(), senha, str)

        cliente = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        id = int(id)
        cliente = Cliente(id, nome="", email="", telef="", senha="")
        ClienteDAO.excluir(cliente)