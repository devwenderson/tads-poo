import streamlit as st
import pandas as pd
from views import View
import time

class ManterEderecoUI:
    def main():
        st.header("Manter enderecos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterEderecoUI.listar()
        with tab2: ManterEderecoUI.cadastrar()
        with tab3: ManterEderecoUI.atualizar()
        with tab4: ManterEderecoUI.excluir()
    
    def listar():
        try:
            pass
        except ValueError as e:
            st.warning(e)
    
    def cadastrar():               
        if st.button("Cadastrar"):
            try:
                pass
            except ValueError as e:
                st.warning(e)

    def atualizar():
        if st.button("Atualizar"):
            try:
                pass
            except ValueError as e:
                st.warning(e)
                

    def excluir():
        if st.button("Excluir"):
            try:
                pass
            except ValueError as e:
                st.warning(e)