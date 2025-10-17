from enum import Enum
from datetime import datetime, timedelta

class Pagamento(Enum):
    EM_ABERTO = "Em aberto"
    PAGO_PARCIAL = "Pago parcialmente"
    PAGO = "Pago"

class Boleto:
    __valorPago = 0
    __dataPgto = None
    __situacao = Pagamento.EM_ABERTO.value

    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.setCodBarras(codBarras)
        self.setDataEmissao(dataEmissao)
        self.setDataVencimento(dataVencimento)
        self.setValorBoleto(valorBoleto)
    
    def __str__(self):
        dataEmissaoFormatada = self.__dataEmissao.strftime("%d/%m/%Y")
        dataVencimentoFormatada = self.__dataVencimento.strftime("%d/%m/%Y")

        dados = ""
        dados += f"Código de barras: {self.__codBarras}\n"
        dados += f"Data de emissão: {dataEmissaoFormatada}\n"
        dados += f"Data de vencimento: {dataVencimentoFormatada}\n"
        dados += f"Valor do boleto: {self.__valorBoleto}\n"
        dados += f"Situação: {self.__situacao}\n"

        if (self.__situacao != Pagamento.EM_ABERTO.value):
            dataPgtoFormatada = self.__dataPgto.strftime("%d/%m/%Y")
            dados += f"Data pagamento: {dataPgtoFormatada}\n"
            dados += f"Valor pago: R$ {self.__valorPago}\n"
        
        return dados

    def setCodBarras(self, codBarras):
        self.__codBarras = codBarras

    def getCodBarras(self):
        return self.__codBarras

    def setDataEmissao(self, dataEmissao):
        self.__dataEmissao = dataEmissao

    def setDataVencimento(self, dataVencimento):
        self.__dataVencimento = dataVencimento

    def setValorBoleto(self, valorBoleto):
        self.__valorBoleto = valorBoleto

    def getDataEmissao(self):
        return self.__dataEmissao
    
    def getDataVencimento(self):
        return self.__dataVencimento

    def getValorBoleto(self):
        return self.__valorBoleto

    def pagar(self, valorPago):
        valorBoleto = self.__valorBoleto
        pgto = valorBoleto - valorPago 
        if (pgto == 0):
            self.__situacao = Pagamento.PAGO.value
        elif (pgto > 0):
            self.__situacao = Pagamento.PAGO_PARCIAL.value
        self.__valorPago = valorPago
        self.__dataPgto = datetime.now().date()
        
    def situacao(self):
        return self.__situacao

dataEmissao = datetime.strptime("10/03/2025", "%d/%m/%Y").date()
mes_seguinte = timedelta(days=30)
dataVencimento = dataEmissao + mes_seguinte

boleto = Boleto("193747119", dataEmissao, dataVencimento, 340)
print("Antes de pagar")
print(boleto)

boleto.pagar(320)
print("Depois de pagar")
print(boleto)
