import streamlit as st
from views.loginView import LoginView

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Email:")
        senha = st.text_input("Senha:", type="password")

        if (st.button("Entrar")):
            c = LoginView.autenticar(email=email, senha=senha)
            if (c == None):
                st.write("Email ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.rerun()
    
    
