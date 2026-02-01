import streamlit as st
import pandas as pd
from views.fornecedorView import FornecedorView
from views.entregaView import EntregaView
from views.produtoView import ProdutoView
import time


class ManterEntregaUI:
    def main():
        st.header("Manter Entregas")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                "Listar",
                "Cadastrar",
                "Atualizar",
                "Excluir",
                "Adicionar Produtos",
                "Editar Produtos",
            ]
        )

        with tab1:
            ManterEntregaUI.listar()
        with tab2:
            ManterEntregaUI.cadastrar()
        with tab3:
            ManterEntregaUI.atualizar()
        with tab4:
            ManterEntregaUI.excluir()
        with tab5:
            ManterEntregaUI.adicionar_produtos()
        with tab6:
            ManterEntregaUI.editar_produto()

    # ---------- LISTAR ----------
    def listar():
        try:
            entregas = EntregaView.entrega_listar()
            produtos_entrega = EntregaView.produto_entrega_listar()
            produtos = ProdutoView.produto_listar()

            for entrega in entregas:
                itens = []

                for pe in produtos_entrega:
                    if pe.getEntregaId() == entrega.getId():
                        for prod in produtos:
                            if prod.getId() == pe.getProdutoId():
                                itens.append(
                                    {
                                        "produto": prod.getDescricao(),
                                        "quantidade": pe.getQuantidadeProduto(),
                                    }
                                )

                st.subheader(f"Entrega #{entrega.getId()}")
                st.write(
                    f"Fornecedor: {entrega.getFornecedor()} | "
                    f"Pedido: {entrega.getDataPedido().strftime('%d/%m/%Y')} | "
                    f"Entrega: {entrega.getDataEntrega().strftime('%d/%m/%Y')}"
                )

                if itens:
                    df = pd.DataFrame(itens)
                    st.dataframe(df, hide_index=True)
                else:
                    st.info("Nenhum produto associado a esta entrega")

                st.divider()

        except ValueError as e:
            st.warning(e)

    # ---------- CADASTRAR ----------
    def cadastrar():
        
            fornecedores = FornecedorView.fornecedor_listar()
            if (len(fornecedores) == 0):
                st.warning("Nenhum fornecedor cadastrado")
            else:
                try:
                    fornecedor = st.selectbox(
                        "Fornecedor",
                        fornecedores,
                        index=None,
                        placeholder="Selecione um fornecedor",
                    )
                    data_pedido = st.date_input("Data do pedido")
                    data_entrega = st.date_input("Data da entrega")

                    if st.button("Cadastrar entrega"):
                        EntregaView.entrega_inserir(
                            fornecedor.getId(), data_pedido, data_entrega
                        )
                        st.success("Entrega cadastrada com sucesso")
                        time.sleep(1)
                        st.rerun()

                except ValueError as e:
                    st.warning(e)

    # ---------- ATUALIZAR ----------
    def atualizar():
        try:
            entregas = EntregaView.entrega_listar()
            fornecedores = FornecedorView.fornecedor_listar()

            op = st.selectbox(
                "Atualização da entrega",
                entregas,
                index=None,
                placeholder="Selecione uma entrega",
            )

            if op:
                fornecedor = st.selectbox("Novo fornecedor", options=fornecedores, index=op.getFornecedor()-1)
                data_pedido = st.date_input("Data do pedido", op.getDataPedido())
                data_entrega = st.date_input("Data da entrega", op.getDataEntrega())

                if st.button("Atualizar"):
                    print(f"Data pedido: {data_pedido}")
                    EntregaView.entrega_atualizar(
                        op.getId(), fornecedor.getId(), data_pedido, data_entrega
                    )
                    st.success("Entrega atualizada")
                    time.sleep(1)
                    st.rerun()

        except ValueError as e:
            st.warning(e)

    # ---------- EXCLUIR ----------
    def excluir():
        try:
            entregas = EntregaView.entrega_listar()

            op = st.selectbox(
                "Excluir entrega",
                entregas,
                index=None,
                placeholder="Selecione uma entrega",
            )

            if op and st.button("Excluir"):
                EntregaView.entrega_excluir(op.getId())
                st.success("Entrega excluída")
                time.sleep(1)
                st.rerun()

        except ValueError as e:
            st.warning(e)

    # ---------- ADICIONAR PRODUTOS ----------
    def adicionar_produtos():
        try:
            entregas = EntregaView.entrega_listar()
            produtos = ProdutoView.produto_listar()

            entrega = st.selectbox(
                "Entrega", entregas, index=None, placeholder="Selecione uma entrega"
            )

            produto = st.selectbox(
                "Produto", produtos, index=None, placeholder="Selecione um produto"
            )

            quantidade = st.number_input("Quantidade", min_value=1, step=1)

            if st.button("Adicionar produto à entrega"):
                EntregaView.produto_entrega_inserir(
                    entrega.getId(), produto.getId(), quantidade
                )
                st.success("Produto adicionado à entrega")
                time.sleep(1)
                st.rerun()

        except ValueError as e:
            st.warning(e)

    def editar_produto():
        try:
            entregas = EntregaView.entrega_listar()
            produtos_entrega = EntregaView.produto_entrega_listar()

            entrega = st.selectbox(
                "Entrega",
                entregas,
                index=None,
                placeholder="Selecione uma entrega",
                key="ent",
            )

            if not entrega:
                return

            vinculados = [
                pe for pe in produtos_entrega if pe.getEntregaId() == entrega.getId()
            ]

            if not vinculados:
                st.info("Esta entrega não possui produtos")
                return

            prod_ent = st.selectbox(
                "Produto da entrega",
                vinculados,
                index=None,
                placeholder="Selecione o produto",
            )

            if not prod_ent:
                return

            nova_qtd = st.number_input(
                "Nova quantidade",
                min_value=1,
                value=prod_ent.getQuantidadeProduto(),
                step=1,
            )

            if st.button("Atualizar quantidade"):
                EntregaView.produto_entrega_atualizar(prod_ent.getId(), nova_qtd)
                st.success("Produto da entrega atualizado")
                time.sleep(1)
                st.rerun()

        except ValueError as e:
            st.warning(e)
