from dao_classes import FornecedorDAO
from models import Fornecedor
from utils import verifica_valor, sucesso_mensagem

class FornecedorView:
    def fornecedor_inserir(cnpj, razao_social):
        try:
            fornecedores = FornecedorDAO.listar()
        except:
            fornecedores = []

        for forne in fornecedores:
            if cnpj == forne.getCNPJ():
                raise ValueError("Fornecedor já existe")
            
        fornecedor = Fornecedor(0, cnpj, razao_social)
        FornecedorDAO.inserir(fornecedor)
        sucesso_mensagem("Fornecedor")
        
    def fornecedor_listar():
        return FornecedorDAO.listar()
    
    def fornecedor_atualizar(id, cnpj, razao_social):
        if not(isinstance(id, int)):
            raise ValueError("o ID precisa ser um inteiro")
        
        fornecedor = Fornecedor(id, cnpj, razao_social)
        FornecedorDAO.atualizar(fornecedor)

    def fornecedor_excluir(id):
        if not(isinstance(id, int)):
            raise ValueError("o ID precisa ser um inteiro")
        
        fornecedor = Fornecedor(id, cnpj="", razao_social="")
        FornecedorDAO.excluir(fornecedor)
        
