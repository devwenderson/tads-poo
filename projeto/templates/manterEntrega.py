import streamlit as st
import pandas as pd
from views import View
import time

class ManterEntregaUI:
    def main():
        st.header("Manter entregas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterEntregaUI.listar()
        with tab2: ManterEntregaUI.cadastrar()
        with tab3: ManterEntregaUI.atualizar()
        with tab4: ManterEntregaUI.excluir()
    
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