from dao_classes import VendaDAO, VendaItemDAO, ProdutoDAO
from models import Venda, VendaItem
from utils import verifica_valor

class VendaView:
    def vendas_listar(is_carrinho=False, carrinho_only=False, cliente_id=None):
        vendas = VendaDAO.listar(is_carrinho=is_carrinho, carrinho_only=carrinho_only, cliente_id=cliente_id)
        itens = VendaItemDAO.listar()
        produtos = ProdutoDAO.listar()

        return {
            "vendas": vendas,
            "itens": itens,
            "produtos": produtos
        }
    
    def vendas_inserir(data, carrinho, cliente_id, produto_id):
        venda = Venda(0, data, carrinho, cliente_id)
        venda.setProdutos(produto_id)
        VendaDAO.inserir(venda)

    def verifica_estoque(produto_id):
        produtos = VendaView.produto_listar()
        for prod in produtos:
            if (prod.getId() == produto_id):
                if (prod.getEstoque() == 0):
                    return False
        return True
    
    def carrinho_inserir(data, carrinho, cliente_id, produto_id, qtd):
        carrinhos = VendaDAO.listar(is_carrinho=True, cliente_id=cliente_id)
        produto_preco = ProdutoDAO.busca_obj(produto_id).getPreco()
        
        for car in carrinhos:
            if car.getCliente() == cliente_id and car.getCarrinho() == True:                
                
                itens = VendaItemDAO.listar(car)
                for it in itens:
                    if (not(VendaView.verifica_estoque(produto_id))):
                        raise ValueError("Sem estoque do produto")
                    
                    if (produto_id == it.getProduto()):
                        it.setQtd(it.getQtd() + qtd) 
                        VendaItemDAO.atualizar(it)
                        return
                        
                item = VendaItem(
                    id=0,
                    qtd=qtd,
                    venda_id=car.getId(),
                    produto_id=produto_id,
                    preco=produto_preco
                )

                VendaItemDAO.inserir(item)                
                return 
                
        carrinho = Venda(0, data, carrinho, cliente_id)
        VendaDAO.inserir(carrinho)
        item = VendaItem(
            id=0,
            qtd=qtd,
            venda_id=carrinho.getId(),
            produto_id=produto_id,
            preco=produto_preco
        )
        VendaItemDAO.inserir(item)                
        return True
    
    def carrinho_visualizar(cliente_id):
        carrinho = None
        for v in VendaView.vendas_listar(is_carrinho=True, cliente_id=cliente_id)["vendas"]:
            if (v.getCarrinho() == True and v.getCliente()==cliente_id): 
                carrinho = v
        
        itens = None
        if carrinho != None:
            itens = VendaItemDAO.listar(carrinho)
        
        produtos = ProdutoDAO.listar()
        
        return {
            "carrinho": carrinho,
            "itens": itens,
            "produtos": produtos
        }
    
    def carrinho_comprar(cliente_id, comprar=False):
        carrinho = VendaView.vendas_listar(is_carrinho=True, carrinho_only=True, cliente_id=cliente_id)["vendas"][0]
        itens = VendaItemDAO.listar(venda=carrinho)
        produtos = VendaView.produto_listar()
        
        for i in itens:
            for p in produtos:
                if i.getProduto() == p.getId():
                    estoque_atual = p.getEstoque()
                    qtd_comprada = i.getQtd()
                    p.setEstoque(estoque_atual - qtd_comprada)
                    ProdutoDAO.atualizar(p)
        
        if comprar:
            carrinho.setCarrinho(False)
            VendaDAO.atualizar(carrinho)
            return {
                "carrinho": None,
                "itens": None,
                "status": True
            }
        
        return {
            "carrinho": carrinho,
            "itens": itens ,
            "status": False
        }

    # NOVA FUNCIONALIDADE
    def carrinho_esvaziar(cliente_id):
        carrinho_dados = VendaView.carrinho_visualizar(cliente_id=cliente_id)
        itens = carrinho_dados["itens"]
        VendaDAO.excluir(carrinho_dados["carrinho"])

        for it in itens:
            VendaItemDAO.excluir(it)