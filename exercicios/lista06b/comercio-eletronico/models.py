from datetime import datetime

class Cliente:
    id = int
    nome = str
    email = str
    telefone = str

    def __init__(self, id, nome, email, telef):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setTelefone(telef)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Nome: {self.nome}\n"
        texto += f"E-mail: {self.email}\n"
        texto += f"Telefone: {self.telefone}\n"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def setTelefone(self, telefone):
        self.telefone = telefone

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

class Categoria:
    id = int
    nome = str

    def __init__(self, id, nome):
        self.setId(id)
        self.setNome(nome)
    
    def __str__(self):
        return f"ID: {self.id:03d} - Nome: {self.nome}\n"

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

class Produto:
    id = int
    descricao = str
    preco = float
    estoque = int
    categoria = Categoria 

    def __init__(self, id, descricao, preco, estoque, categoria):
        self.setId(id)
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setCategoria(categoria)
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Descrição: {self.descricao}\n"
        texto += f"Preço: R$ {self.preco:0.2f}\n"
        texto += f"Estoque: {self.estoque}\n"
        texto += f"Categoria: {self.categoria.getNome()}\n"
        return texto


    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setPreco(self, preco):
        self.preco = preco

    def setEstoque(self, estoque):
        self.estoque = estoque

    def setCategoria(self, categoria):
        self.categoria = categoria

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getDescricao(self):
        return self.descricao

    def getPreco(self):
        return self.preco

    def getEstoque(self):
        return self.estoque

    def getCategoria(self):
        return self.categoria

class Venda:
    id = int
    data = datetime
    carrinho = bool
    total = float
    cliente = Cliente
    produtos = []

    def __init__(self, id: int, data: datetime, carrinho: bool, cliente: Cliente):
        self.setId(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setCliente(cliente)
        self.setTotal()
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Data da venda: {self.data.strftime("%d/%m/%Y")}\n"
        texto += f"Carrinho: {self.carrinho}\n"
        texto += f"Total: R$ {self.total:0.2f}\n"
        texto += f"Cliente: {self.cliente.getNome()}\n"
        texto += "Produtos: \n"
        for p in self.produtos:
            texto += f" - {p.getProduto().getDescricao()}\n"

        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.data = data

    def setCarrinho(self, carrinho):
        self.carrinho = carrinho

    def setTotal(self):
        total = 0
        for p in self.produtos:
            total += p.getPreco()
        self.total = total

    def setCliente(self, cliente):
        self.cliente = cliente
    
    def setProdutos(self, prod):
        self.produtos.append(prod)
        self.setTotal()

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getCarrinho(self):
        return self.carrinho

    def getTotal(self):
        return self.total

    def getCliente(self):
        return self.cliente

    def getProdutos(self):
        return self.produtos

class VendaItem:
    id = int
    qtd = int
    preco = float
    venda = Venda
    __produto = Produto

    def __init__(self, id: int, qtd: int, venda: Venda, produto: Produto):
        self.setId(id)
        self.setQtd(qtd)
        self.setVenda(venda)
        self.setProduto(produto)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Produto: {self.produto.getDescricao()}\n"
        texto += f"Quantidade: {self.qtd}\n"
        texto += f"Preço Unitário: R$ {self.produto.getPreco():0.2f}\n"
        texto += f"Subtotal: R$ {self.preco:0.2f}\n"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setQtd(self, qtd):
        self.qtd = qtd

    def setPreco(self):
        produto = self.produto
        preco = self.qtd * produto.getPreco()
        self.preco = preco

    def setVenda(self, venda):
        self.venda = venda

    def setProduto(self, produto):
        self.produto = produto
        self.setPreco()

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getQtd(self):
        return self.qtd

    def getPreco(self):
        return self.preco

    def getVenda(self):
        return self.venda

    def getProduto(self):
        return self.produto




