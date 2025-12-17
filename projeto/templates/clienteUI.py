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
    
    def inserir_produto_carrinho():
        st.subheader("Inserir produto no carrinho")      
        carrinho = View.carrinho_visualizar(
            cliente_id=st.session_state["cliente_id"]
        )
    
        produtos = View.produto_listar()
        produto = st.selectbox("Produto", produtos)
        qtd = st.number_input("Quantidade", value=1)
        
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
        
    def visualizar_carrinho():
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

            if (st.button("Finalizar compra")):
                
                dados = View.carrinho_comprar(
                    cliente_id=st.session_state["cliente_id"],
                    comprar=True    
                )              
                st.success("Compra finalizada")
                time.sleep(2)
                st.rerun()


            if (st.button("Esvaziar carrinho")):
                View.carrinho_esvaziar(st.session_state["cliente_id"])
                st.success("Esvaziando...")
                time.sleep(2)
                st.rerun()
        else:
            st.write("Carrinho vazio")

                
    def listar_minhas_compras():
        st.subheader("Minhas compras")
        dados = View.vendas_listar(
            is_carrinho=False, 
            cliente_id=st.session_state["cliente_id"]
        )
        for venda in dados["vendas"]:
            prod_list_dict = []
            preco_total = 0
            cliente = st.session_state["cliente_nome"]
            data = venda.getData().strftime("%d/%m/%Y")
            venda_id = venda.getId()
            for item in dados["itens"]:
                if (item.getVenda() == venda.getId()):
                    for prod in dados["produtos"]:
                        if (prod.getId() == item.getProduto()):
                            prod_dict = {}
                            prod_dict["produto"] = prod.getDescricao()
                            prod_dict["quantidade"] = item.getQtd()
                            prod_dict["preco_unitario"] = item.getPreco()
                            prod_dict["subtotal"] = prod_dict["preco_unitario"] * prod_dict["quantidade"]
                            preco_total = preco_total + prod_dict["subtotal"]
                            prod_list_dict.append(prod_dict)
            
            st.write(f"Venda: {venda_id} | Cliente: {cliente} | Realização da venda: {data}")
            df = pd.DataFrame(prod_list_dict)
            st.dataframe(df, hide_index=True, column_order=["produto", "quantidade", "preco_unitario", "subtotal"])
            st.write(f"Total: R${preco_total:0.2f}")