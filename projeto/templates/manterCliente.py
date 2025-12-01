import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de cliente")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.cadastrar()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    
    def listar():
        st.subheader("Clientes")
        clientes = View.cliente_listar()

        if (len(clientes) == 0):
            st.write("Nenhum cliente cadastrado")
        else:
            list_dict = []
            for obj in clientes:
                list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "telefone"])
    
    def cadastrar():
        st.subheader("Cadastrar")   
                
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        telefone = st.text_input("Telefone")

        if st.button("Cadastrar"):
            for c in View.cliente_listar():
                if c.getEmail() == email:
                    st.warning("Cliente já existe")
                    time.sleep(2)
                    st.rerun()
            
            View.cliente_inserir(nome, email, senha, telefone)
            st.success("Cliente cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        st.subheader("Atualizar")

    def excluir():
        st.subheader("Excluir")