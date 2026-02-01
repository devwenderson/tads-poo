import streamlit as st
import pandas as pd
from utils import sucesso_mensagem
from views.fornecedorView import FornecedorView
import time

class ManterFornecedorUI:
    def main():
        st.header("Manter fornecedores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterFornecedorUI.listar()
        with tab2: ManterFornecedorUI.cadastrar()
        with tab3: ManterFornecedorUI.atualizar()
        with tab4: ManterFornecedorUI.excluir()
    
    def listar():
        st.subheader("Fornecedores")
        try:
            fornecedores = FornecedorView.fornecedor_listar()
            if (len(fornecedores) == 0):
                st.warning("Nenhum fornecedor cadastrado")
            else:
                forne_dict_list = []

                for forne in fornecedores:
                    forne_dict_list.append(forne.to_json())

                df = pd.DataFrame(forne_dict_list)
                st.dataframe(df, hide_index=True, column_order=["id", "cnpj", "razao_social"])
        except ValueError as e:
            st.warning(e)
    
    def cadastrar():       
        st.subheader("Cadastrar")

        cnpj = st.text_input("CNPJ")
        razao_social = st.text_input("Razão social")

        if st.button("Cadastrar"):
            try:
                FornecedorView.fornecedor_inserir(cnpj, razao_social)
                sucesso_mensagem("Fornecedor")
            except ValueError as e:
                st.warning(e)

    def atualizar():
        st.subheader("Atualizar")
        fornecedores = FornecedorView.fornecedor_listar()

        if (len(fornecedores)) == 0:
            st.warning("Nenhum fornecedor cadastrado")
        else:
            op = st.selectbox("Atualização de fornecedor", 
                              options=fornecedores, 
                              placeholder="Selecione um fornecedor", 
                              index=None)
            if (op is not None):
                cnpj = st.text_input("Novo CNPJ", op.getCNPJ())
                razao_social = st.text_input("Nova Razão social", op.getRazaoSocial())
                if st.button("Atualizar"):
                    try:
                        id_forne = op.getId()
                        FornecedorView.fornecedor_atualizar(id_forne, cnpj, razao_social)
                        sucesso_mensagem("Fornecedor")
                    except ValueError as e:
                        st.warning(e)
                

    def excluir():
        st.subheader("Excluir")
        fornecedores = FornecedorView.fornecedor_listar()

        if (len(fornecedores)) == 0:
            st.warning("Nenhum fornecedor cadastrado")
        else:
            op = st.selectbox("Excluir fornecedor", 
                              options=fornecedores, 
                              placeholder="Selecione um fornecedor", 
                              index=None)
            
            if (op is not None):
                if st.button("Excluir"):
                    try:
                        id_forne = op.getId()
                        FornecedorView.fornecedor_excluir(id_forne)
                        sucesso_mensagem("Fornecedor")
                    except ValueError as e:
                        st.warning(e)