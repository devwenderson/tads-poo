from templates.manterCliente import ManterClienteUI
from templates.manterCategoria import ManterCategoriaUI
from templates.manterProduto import ManterProdutoUI
from templates.manterVenda import ManterVendaUI
from templates.login import LoginUI
from templates.clienteUI import ClienteUI
from views import View
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no sistema",
            "Criar conta",
        ])

        if op == "Entrar no sistema": LoginUI.main()
        if op == "Criar conta": ManterClienteUI.cadastrar()  

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos",
            "Carrinho",
            "Listar minhas compras",
            "Sair"
        ])

        if op == "Listar produtos": ManterProdutoUI.listar()
        if op == "Carrinho": ClienteUI.carrinho()
        if op == "Listar minhas compras": ClienteUI.listar_minhas_compras()
        if op == "Sair": IndexUI.logout()   

    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de clientes",
            "Cadastro de categorias",
            "Cadastro de produtos",
            "Cadastro de vendas",
            "Reajustar produtos",
            "Sair"
        ])

        if op == "Cadastro de categorias": ManterCategoriaUI.main()
        if op == "Cadastro de clientes": ManterClienteUI.main()
        if op == "Cadastro de produtos": ManterProdutoUI.main()
        if op == "Cadastro de vendas": ManterVendaUI.main()
        if op == "Reajustar produtos": ManterProdutoUI.main()
        if op == "Sair": IndexUI.logout()

    def logout():
        del st.session_state["cliente_id"]
        del st.session_state["cliente_nome"]
        st.rerun()         
    
    def sidebar():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            nome = st.session_state["cliente_nome"]
            st.write(f"Bem-vindo(a), {nome}")
            if nome == "admin": 
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
    
    def main():
        View.criar_admin()
        IndexUI.sidebar()
    
IndexUI.main()