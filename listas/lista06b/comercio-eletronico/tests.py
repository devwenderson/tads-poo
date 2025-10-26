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
smartphone = Produto(3, "Smartphone", 1000, 30, eletr)
notebook = Produto(4, "Notebook", 3999.00, 15, inform)
fone = Produto(5, "Fone de Ouvido Bluetooth", 299.99, 50, eletr)
mouse = Produto(6, "Mouse Gamer", 149.90, 40, eletr)

# ------ VENDAS ----------
venda1 = Venda(101, datetime(2025, 10, 15), False, joao.getId())
venda2 = Venda(102, datetime(2025, 10, 16), False, ana.getId())

# ------ ITENS VENDAS ----------
item_1_venda_1 = VendaItem(1, 2, venda1, smartphone, smartphone.getPreco())
item_2_venda_1 = VendaItem(2, 3, venda1, mouse, mouse.getPreco())
itens_venda_1 = [item_1_venda_1, item_2_venda_1]

# ------ ADICIONA ITENS NAS VENDAS ----------
for item in itens_venda_1:
    venda1.setProdutos(item.getId())

print(venda1)