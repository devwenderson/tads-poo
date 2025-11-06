# === PARA FAZER A VERIFICAÇÃO DAS ENTRADAS ===
def verifica_valor(antigo, novo, conversor=str):
    if novo in [None, '', ' ']: return antigo
    else: return conversor(novo)