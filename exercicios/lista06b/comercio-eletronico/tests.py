from models import Cliente, Produto, Venda, VendaItem, Categoria
from datetime import datetime

# ------ CLIENTES ----------
joao = Cliente(1, "João Silva", "joao.silva@email.com", "(11) 98765-4321")
ana = Cliente(2, "Ana Souza", "ana.souza@email.com", "(21) 99988-7766")

# ------ CATEGORIAS ----------
escr = Categoria(1, "Escritório")        
limp = Categoria(2, "Limpeza")
eletr = Categoria(3, "Eletrônico")
inform = Categoria(4, "Informática")

# ------ PRODUTOS ----------
amacian = Produto(1, "Amaciante", 5.5, 200, limp)
lapis = Produto(2, "Lápis", 1.25, 500, escr)
smartphone = Produto(1, "Smartphone", 1999.90, 30, eletr)
notebook = Produto(2, "Notebook", 3999.00, 15, inform)
fone = Produto(3, "Fone de Ouvido Bluetooth", 299.99, 50, eletr)
mouse = Produto(4, "Mouse Gamer", 149.90, 40, eletr)

# ------ VENDAS ----------
venda1 = Venda(101, datetime(2025, 10, 15, 14, 30), False, 250.00, joao)
venda2 = Venda(102, datetime(2025, 10, 16, 10, 45), False, 120.00, ana)

# ------ ITENS VENDAS ----------
item_1_venda_1 = VendaItem(1, 2, smartphone.getPreco() * 2, venda1, smartphone)
item_2_venda_1 = VendaItem(2, 3, mouse.getPreco() * 3, venda1, mouse)
itens_venda_1 = [item_1_venda_1, item_2_venda_1]

# ------ ADICIONA ITENS NAS VENDAS ----------
for item in itens_venda_1:
    venda1.setProdutos(item)

print(venda1)