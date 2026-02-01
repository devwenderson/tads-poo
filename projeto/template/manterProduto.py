import streamlit as st
import pandas as pd
from views.produtoView import ProdutoView
from views.categoriaView import CategoriaView
import time


class ManterProdutoUI:
    def main():
        st.header("Manter produto")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["Listar", "Cadastrar", "Atualizar", "Excluir", "Reajustar preço"]
        )

        with tab1:
            ManterProdutoUI.listar()
        with tab2:
            ManterProdutoUI.cadastrar()
        with tab3:
            ManterProdutoUI.atualizar()
        with tab4:
            ManterProdutoUI.excluir()
        with tab5:
            ManterProdutoUI.reajustar_preco()

    def listar():
        st.subheader("Produtos")
        try:
            produtos = ProdutoView.produto_listar()
            categorias = CategoriaView.categoria_listar()

            prod_list_dict = []
            cat_list_dict = []

            for obj in produtos:
                prod_list_dict.append(obj.to_json())

            for obj in categorias:
                cat_list_dict.append(obj.to_json())

            # SUBSTITUIR ID DA CATEGORIA PELO NOME
            for pro in prod_list_dict:
                for cat in cat_list_dict:
                    if cat["id"] == pro["categoria"]:
                        pro["categoria"] = cat["nome"]

            df = pd.DataFrame(prod_list_dict)
            st.dataframe(
                df,
                hide_index=True,
                column_order=["id", "descricao", "preco", "estoque", "categoria"],
            )
        except ValueError as e:
            st.warning(e)

    def cadastrar():
        st.subheader("Cadastrar produto")
        categorias = CategoriaView.categoria_listar()
        descricao = st.text_input("Nome")
        preco = st.number_input("Preco")
        estoque = st.number_input("Estoque", value=0)
        categoria = st.selectbox("Categoria", categorias)

        if st.button("Cadastrar"):
            for c in ProdutoView.produto_listar():
                if c.getDescricao() == descricao:
                    st.warning("Produto já existe")
                    time.sleep(2)
                    st.rerun()

            try:
                ProdutoView.produto_inserir(
                    descricao, preco, estoque, categoria.getId()
                )
                st.success("Produto cadastrado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def atualizar():
        produtos = ProdutoView.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")

        op = st.selectbox("Atualização do cliente", produtos)
        categorias = CategoriaView.categoria_listar()
        descricao = st.text_input("Nova descrição", op.getDescricao())
        preco = st.number_input("Novo preço", op.getPreco())
        estoque = st.number_input("Novo estoque", op.getEstoque())
        categoria = st.selectbox(
            "Nova categoria", options=categorias, index=op.getCategoria() - 1
        )

        if st.button("Atualizar"):
            pro_id = op.getId()
            cat_id = categoria.getId()

            if categoria == None:
                cat_id = op.getCategoria()

            try:
                ProdutoView.produto_atualizar(pro_id, descricao, preco, estoque, cat_id)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def excluir():
        produtos = ProdutoView.produto_listar()

        op = st.selectbox("Excluir produtos", produtos)
        if st.button("Excluir"):
            prod_id = op.getId()

            ProdutoView.produto_excluir(prod_id)
            st.success("Produto excluído com sucesso")
            time.sleep(2)
            st.rerun()

    def reajustar_preco():
        percentual = st.number_input("Percentual", value=0)
        if st.button("Reajustar"):
            try:
                ProdutoView.produto_reajustar(percentual=percentual)
                st.success("Preços reajustados com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
