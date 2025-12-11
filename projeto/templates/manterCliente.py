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
        try:
            clientes = View.cliente_listar()
            list_dict = []
            for obj in clientes:
                list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            st.dataframe(df, hide_index=True, column_order=["id", "nome", "email", "telefone"])
        except ValueError as e:
            st.warning(e)
    
    def cadastrar():
        st.subheader("Cadastrar")   
                
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        telefone = st.text_input("Telefone")

        if st.button("Cadastrar"):
            try:
                View.cliente_inserir(nome, email, senha, telefone)
                st.success("Cliente cadastrado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
            
            

    def atualizar():
        clientes = View.cliente_listar()
        if (len(clientes) == 0): 
            st.write("Nenhum cliente cadastrado")
        op = st.selectbox("Atualização do cliente", clientes)
        nome = st.text_input("Novo nome", op.getNome())
        email = st.text_input("Novo email", op.getEmail())
        senha = st.text_input("Nova senha", op.getSenha())
        telefone = st.text_input("Novo telefone", op.getTelefone())

        if st.button("Atualizar"):
            try:
                cli_id = op.getId()
                View.cliente_atualizar(cli_id, nome, email, telefone, senha)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.warning(e)
                

    def excluir():
        clientes = View.cliente_listar()
        op = st.selectbox("Excluir cliente", clientes)

        if st.button("Excluir"):
            cli_id = op.getId()
            View.cliente_excluir(cli_id)
            st.success("Cliente excluído com sucesso")
            time.sleep(2)
            st.rerun()