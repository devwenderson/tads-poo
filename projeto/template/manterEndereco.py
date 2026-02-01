import streamlit as st
import pandas as pd
from views.clienteView import ClienteView
from views.enderecoView import EnderecoView
import time
from utils import sucesso_cadastro

class ManterEderecoUI:
    def main():
        st.header("Manter enderecos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Cadastrar", "Atualizar", "Excluir"])

        with tab1: ManterEderecoUI.listar()
        with tab2: ManterEderecoUI.cadastrar()
        with tab3: ManterEderecoUI.atualizar()
        with tab4: ManterEderecoUI.excluir()
    
    def listar():
        st.subheader("Endereços")
        try:
            enderecos = EnderecoView.endereco_listar()
            clientes = ClienteView.cliente_listar()

            if (len(enderecos) == 0):
                st.warning("Nenhum endereço cadastrado")
            else:
                cli_list_dict = []
                ender_list_dict = []

                for obj in enderecos:
                    ender_list_dict.append(obj.to_json())

                for obj in clientes:
                    cli_list_dict.append(obj.to_json())

                for ender in ender_list_dict:
                    for cli in cli_list_dict:
                        if cli["id"] == ender["id_cliente"]:
                            ender["id_cliente"] = cli["nome"]

                df = pd.DataFrame(ender_list_dict)
                st.dataframe(df, hide_index=True, column_order=["id", "id_cliente", "logradouro", "numero", "cidade", "estado"])
        except ValueError as e:
            st.warning(e)
    
    def cadastrar():        
        st.subheader("Cadastrar")
        clientes = ClienteView.cliente_listar()
        logradouro = st.text_input("Logradouro")
        num_casa =  st.text_input("Número")
        complemento = st.text_input("Complemento")
        bairro = st.text_input("Bairro")
        cidade = st.text_input("Cidade")
        estado = st.text_input("Estado")
        cep = st.text_input("CEP")  
        cli = st.selectbox("Cliente", clientes, placeholder="Selecione o cliente", index=None)

        if st.button("Cadastrar"):
            try:
                EnderecoView.endereco_inserir(logradouro, num_casa, complemento, bairro, cidade, estado, cep, cli.getId())
                sucesso_cadastro("Endereço")

            except ValueError as e:
                st.warning(e)

    def atualizar():
        st.subheader("Atualizar")

        enderecos = EnderecoView.endereco_listar()

        if (len(enderecos) == 0):
            st.write("Nenhum endereço cadastrado")
        
        else:
            clientes = ClienteView.cliente_listar()
            op = st.selectbox("Atualização do endereço", enderecos, index=None, placeholder="Selecione um endereço")
            if (op is not None):
                logradouro = st.text_input("Novo logradouro", op.getLogradouro())
                num_casa =  st.text_input("Novo número", op.getNumero())
                complemento = st.text_input("Novo complemento", op.getComplemento())
                bairro = st.text_input("Novo bairro", op.getBairro())
                cidade = st.text_input("Nova cidade", op.getCidade())
                estado = st.text_input("Novo Estado", op.getEstado())
                cep = st.text_input("Novo CEP", op.getCep())    
                cli = st.selectbox("Novo cliente", clientes, index=op.getIdCliente()-1)

                if st.button("Atualizar"):
                    try:
                        id_endereco = op.getId()
                        EnderecoView.endereco_atualizar(id_endereco, logradouro, num_casa, 
                                                        complemento, bairro, cidade, estado, cep, cli.getId())
                        sucesso_cadastro("Endereço")

                    except ValueError as e:
                        st.warning(e)
                

    def excluir():
        st.subheader("Excluir")
        enderecos = EnderecoView.endereco_listar()
        op = st.selectbox("Excluir endereço", enderecos)

        if st.button("Excluir"):
            try:
                EnderecoView.endereco_excluir(op.getId())
                sucesso_cadastro("Endereço")
            except ValueError as e:
                st.warning(e)