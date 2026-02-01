from template.manterCliente import ManterClienteUI
from template.manterCategoria import ManterCategoriaUI
from template.manterProduto import ManterProdutoUI
from template.manterVenda import ManterVendaUI
from template.manterEndereco import ManterEderecoUI
from template.manterEntrega import ManterEntregaUI
from template.login import LoginUI
from template.clienteUI import ClienteUI
from views.loginView import LoginView
import streamlit as st


class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Entrar no sistema",
                "Criar conta",
            ],
        )

        if op == "Entrar no sistema":
            LoginUI.main()
        if op == "Criar conta":
            ManterClienteUI.cadastrar()

    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu", ["Listar produtos", "Carrinho", "Listar minhas compras", "Sair"]
        )

        if op == "Listar produtos":
            ManterProdutoUI.listar()
        if op == "Carrinho":
            ClienteUI.carrinho()
        if op == "Listar minhas compras":
            ClienteUI.listar_minhas_compras()
        if op == "Sair":
            IndexUI.logout()

    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de clientes",
                "Cadastro de categorias",
                "Cadastro de produtos",
                "Cadastro de vendas",
                "Cadastro de endereços",
                "Cadastro de Entregas",
                "Sair",
            ],
        )

        if op == "Cadastro de categorias":
            ManterCategoriaUI.main()
        if op == "Cadastro de clientes":
            ManterClienteUI.main()
        if op == "Cadastro de produtos":
            ManterProdutoUI.main()
        if op == "Cadastro de vendas":
            ManterVendaUI.main()
        if op == "Cadastro de endereços":
            ManterEderecoUI.main()
        if op == "Cadastro de Entregas":
            ManterEntregaUI.main()
        if op == "Sair":
            IndexUI.logout()

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
        LoginView.criar_admin()
        IndexUI.sidebar()


IndexUI.main()
