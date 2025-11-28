from templates.manterCliente import ManterClienteUI
from templates.manterCategoria import ManterCategoriaUI
from templates.manterProduto import ManterProdutoUI
from templates.manterVenda import ManterVendaUI
import streamlit as st
class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de clientes",
            "Cadastro de categorias",
            "Cadastro de Produtos",
            "Reajustar produtos"
        ])

        if op == "Cadastro de categorias": ManterCategoriaUI.main()
        if op == "Cadastro de clientes": ManterClienteUI.main()
        if op == "Cadastro de produtos": ManterProdutoUI.main()
        if op == "Reajustar produtos": ManterProdutoUI.main()
    
    def sidebar():
        IndexUI.menu_admin()
    
    def main():
        IndexUI.sidebar()
    
IndexUI.main()