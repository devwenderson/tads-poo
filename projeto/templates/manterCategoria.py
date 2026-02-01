import streamlit as st
import pandas as pd
from views.categoriaView import CategoriaView
import time

class ManterCategoriaUI:
    def main():
        st.header("Manter categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.cadastrar()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()
    
    def listar():
        try:
            categorias = CategoriaView.categoria_listar()
            list_dict = []
            for obj in categorias:
                list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            st.dataframe(df, hide_index=True, column_order=["id", "nome"])
        except ValueError as e:
            st.warning(e)
    
    def cadastrar():               
        nome = st.text_input("Nome")

        if st.button("Cadastrar"):
            try:
                CategoriaView.categoria_inserir(nome)
                st.success("Categoria cadastrada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)

    def atualizar():
        categorias = CategoriaView.categoria_listar()
        if (len(categorias) == 0): 
            st.write("Nenhum cliente cadastrado")
        op = st.selectbox("Atualização da categoria", categorias)
        nome = st.text_input("Novo nome", op.getNome())

        if st.button("Atualizar"):
            try:
                id = op.getId()
                CategoriaView.categoria_atualizar(id, nome)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
                

    def excluir():
        categorias = CategoriaView.categoria_listar()
        op = st.selectbox("Excluir categoria", categorias)

        if st.button("Excluir"):
            cat_id = op.getId()

            try:
                CategoriaView.categoria_excluir(cat_id)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)