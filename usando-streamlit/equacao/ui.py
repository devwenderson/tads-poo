from equacao import Equacao2Grau
import streamlit as st
import pandas as pd

class UI:    
    @staticmethod
    def main():
        UI.create_equacao()
        
    @staticmethod
    def create_equacao():
        a = st.number_input("A: ", value=0, on_change=None)
        b = st.number_input("B: ", value=0, on_change=None)
        c = st.number_input("C: ", value=0, on_change=None)

        if (st.button("Calcular")):
            f = Equacao2Grau(a, b, c)

            st.subheader(f"Dados da esquação {a}x**2 + {b}x + {c}")
            st.write(f)
            
            p = f.vertice()

            xmin = p - 10
            xmax = p + 10

            qtd_pontos = 50
            dist = (xmax - xmin) / (qtd_pontos - 1)

            x = xmin
            px = []
            py = []
            while x <= xmax:
                px.append(x)
                py.append(f.y(x))
                x += dist
            df = pd.DataFrame({"x": px, "y": py})
            st.line_chart(df, x="x", y="y")



UI.main()