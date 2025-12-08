import streamlit as st
import pandas as pd
from views import View
from datetime import datetime
import time

class ClienteUI:   
    def carrinho():
        st.header("Carrinho")
        tab1, tab2 = st.tabs(["Inserir produto", "Visualizar"])

        with tab1: ClienteUI.inserir_produto_carrinho()
        with tab2: ClienteUI.visualizar_carrinho()
    
    @classmethod
    def inserir_produto_carrinho(cls):
        st.subheader("Inserir produto no carrinho")      
        carrinho = View.carrinho_visualizar(
            cliente_id=st.session_state["cliente_id"]
        )
    
        produtos = View.produto_listar()
        produto = st.selectbox("Produto", produtos)
        qtd = st.number_input("Quantidade", value=0)
        
        if (st.button("Inserir")):
            if carrinho["carrinho"] != None:
                View.carrinho_inserir(
                    data="",
                    carrinho=True,
                    cliente_id=st.session_state["cliente_id"],
                    produto_id=produto.getId(),
                    qtd=qtd
                )

                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()

            else:
                data = datetime.now()
                carrinho = True
                
                View.carrinho_inserir(
                    data=data,
                    carrinho=carrinho,
                    cliente_id=st.session_state["cliente_id"],
                    produto_id=produto.getId(),
                    qtd=qtd
                )
                st.success("Produto inserido com sucesso")
                time.sleep(2)
                st.rerun()
        
    @classmethod
    def visualizar_carrinho(cls):
        st.subheader("Seu carrinho")
        dados = View.carrinho_visualizar(
            cliente_id=st.session_state["cliente_id"]
        )
        
        if dados["carrinho"] != None: 
           
            carrinho = dados["carrinho"]
            cliente = carrinho.getCliente()
            data = carrinho.getData().strftime('%d/%m/%Y')
            preco_total = 0
            prod_list_dict = []

            for item in dados["itens"]:
                for prod in dados["produtos"]:
                    if (prod.getId() == item.getProduto()):
                        prod_dict = {}
                        prod_dict["produto"] = prod.getDescricao()
                        prod_dict["quantidade"] = item.getQtd()
                        prod_dict["preco_unitario"] = item.getPreco()
                        prod_dict["subtotal"] = prod_dict["preco_unitario"] * prod_dict["quantidade"]
                        preco_total = preco_total + prod_dict["subtotal"]
                        prod_list_dict.append(prod_dict)

            
            st.write(f"Carrinho: Cliente: {cliente} - Criação do carrinho: {data}")
            df = pd.DataFrame(prod_list_dict)
            st.dataframe(df, hide_index=True, column_order=["produto", "quantidade", "preco_unitario", "subtotal"])
            st.write(f"Total: R${preco_total:0.2f}")

                
    def listar_minhas_compras():
        st.subheader("Minhas compras")