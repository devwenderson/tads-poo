import streamlit as st
import time

# === PARA FAZER A VERIFICAÇÃO DAS ENTRADAS ===
def verifica_valor(antigo, novo, conversor=str):
    if novo in [None, '', ' ']: return antigo
    else: return conversor(novo)


def sucesso_mensagem(obj_type):
    st.success(f"{obj_type} Sucesso!")
    time.sleep(2)
    st.rerun()