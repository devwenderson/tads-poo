import streamlit as st
import pandas as pd
from views import View
from datetime import datetime
import time

class ManterVendaUI:
    def main():
        st.header("Vendas")
        tab1 = st.tabs(["Listar"])

        with tab1: ManterVendaUI.listar()

    def listar():
        st.subheader("Vendas")
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