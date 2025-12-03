import streamlit as st
import pandas as pd
from views import View
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
        categorias = View.categoria_listar()

        if (len(categorias) == 0):
            st.write("Nenhuma categoria cadastrada")
        else:
            list_dict = []
            for obj in categorias:
                list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            st.dataframe(df, hide_index=True, column_order=["id", "nome"])
    
    def cadastrar():               
        nome = st.text_input("Nome")

        if st.button("Cadastrar"):
            for c in View.categoria_listar():
                if c.getNome() == nome:
                    st.warning("Categoria já existe")
                    time.sleep(2)
                    st.rerun()
            
            View.categoria_inserir(nome)
            st.success("Categoria cadastrada com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.categoria_listar()
        if (len(categorias) == 0): 
            st.write("Nenhum cliente cadastrado")
        op = st.selectbox("Atualização da categoria", categorias)
        nome = st.text_input("Novo nome", op.getNome())

        if st.button("Atualizar"):
            id = op.getId()
            View.categoria_atualizar(id, nome)
            st.success("Categoria atualizada com sucesso")
            time.sleep(2)
            st.rerun()
                

    def excluir():
        categorias = View.categoria_listar()
        produtos = View.produto_listar()

        op = st.selectbox("Excluir categoria", categorias)

        if st.button("Excluir"):
            cat_id = op.getId()

            for pro in produtos:
                if cat_id == pro.getCategoria():
                    st.error("Essa categoria está sendo usada")
                    time.sleep(2)
                    st.rerun()
            
            View.categoria_excluir(cat_id)
            st.success("Categoria excluída com sucesso")
            time.sleep(2)
            st.rerun()