from dao_classes import EnderecoDAO
from models import Endereco
from utils import verifica_valor

class EnderecoView:
    def endereco_inserir(logradouro, num_casa, complemento, bairro, cidade, estado, cep, id_cliente):
        try:
            enderecos = EnderecoView.endereco_listar()
        except ValueError:
            enderecos = []

        for ender in enderecos:
            if num_casa == ender.getNumero():
                raise ValueError("Endereço já existe")

        endereco = Endereco(0, logradouro, num_casa, complemento, 
                    bairro, cidade, estado, cep, id_cliente)
        
        EnderecoDAO.inserir(endereco)
    
    def endereco_listar():
        return EnderecoDAO.listar()
    
    def endereco_atualizar(id, logradouro, num_casa, complemento, bairro, cidade, estado, cep, id_cliente):
        if not(isinstance(id, int)):
            raise ValueError("o ID precisa ser um inteiro")
        
        endereco = Endereco(id, logradouro, num_casa, complemento, 
                    bairro, cidade, estado, cep, id_cliente)
        
        EnderecoDAO.atualizar(endereco)

    def endereco_excluir(id):
        if not(isinstance(id, int)):
            raise ValueError("o ID precisa ser um inteiro")
        
        endereco = Endereco(id, logradouro="", numero="", complemento="", 
                    bairro="", cidade="", estado="", cep="", id_cliente=0)
        EnderecoDAO.excluir(endereco)       
        