from dao_classes import EntregaDAO, ProdutoEntregaDAO
from models import Entrega, ProdutoEntrega
from utils import verifica_valor
from datetime import datetime


class EntregaView:

    @staticmethod
    def entrega_inserir(
        fornecedor_id: int, data_pedido: datetime, data_entrega: datetime
    ):
        if not isinstance(fornecedor_id, int):
            raise ValueError("Fornecedor inválido")

        if data_entrega < data_pedido:
            raise ValueError("Data de entrega não pode ser anterior à data do pedido")

        entrega = Entrega(
            id=0,
            forn=fornecedor_id,
            dt_p=data_pedido,
            dt_e=data_entrega,
        )

        EntregaDAO.inserir(entrega)

    @staticmethod
    def entrega_listar():
        return EntregaDAO.listar()

    @staticmethod
    def entrega_buscar_por_id(id: int):
        if not isinstance(id, int):
            raise ValueError("ID inválido")

        entrega = EntregaDAO.busca_obj(id)
        if entrega is None:
            raise ValueError("Entrega não encontrada")

        return entrega

    @staticmethod
    def entrega_atualizar(
        id: int,
        fornecedor_id: int,
        data_pedido: datetime,
        data_entrega: datetime,
    ):
        if not isinstance(id, int):
            raise ValueError("ID inválido")

        if data_entrega < data_pedido:
            raise ValueError("Data de entrega não pode ser anterior à data do pedido")

        entrega = Entrega(
            id=id,
            forn=fornecedor_id,
            dt_p=data_pedido,
            dt_e=data_entrega,
        )

        EntregaDAO.atualizar(entrega)

    @staticmethod
    def entrega_excluir(id: int):
        if not isinstance(id, int):
            raise ValueError("ID inválido")

        itens = ProdutoEntregaDAO.listar()
        for item in itens:
            if item.getEntregaId() == id:
                ProdutoEntregaDAO.excluir(item)

        entrega = Entrega(
            id=id,
            forn=0,
            dt_p=datetime.now(),
            dt_e=datetime.now(),
        )

        EntregaDAO.excluir(entrega)

    # PROTUDOS
    @staticmethod
    def produto_entrega_inserir(produto_id: int, entrega_id: int, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        prod_ent = ProdutoEntrega(
            id=0,
            pro_id=produto_id,
            ent_id=entrega_id,
            qtd_pro=quantidade,
        )

        ProdutoEntregaDAO.inserir(prod_ent)

    @staticmethod
    def produto_entrega_listar():
        return ProdutoEntregaDAO.listar()

    @staticmethod
    def produto_entrega_excluir(id: int):
        prod_ent = ProdutoEntrega(
            id=id,
            pro_id=0,
            ent_id=0,
            qtd_pro=0,
        )

        ProdutoEntregaDAO.excluir(prod_ent)
