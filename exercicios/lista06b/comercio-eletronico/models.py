from datetime import datetime

class Cliente:
    __id = int
    __nome = str
    __email = str
    __telefone = str

    def __init__(self, id, nome, email, telef):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setTelefone(telef)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.__id:03d}\n"
        texto += f"Nome: {self.__nome}\n"
        texto += f"E-mail: {self.__email}\n"
        texto += f"Telefone: {self.__telefone}"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome

    def setEmail(self, email):
        self.__email = email

    def setTelefone(self, telefone):
        self.__telefone = telefone

    # --------- GETTERS ---------
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getTelefone(self):
        return self.__telefone

class Categoria:
    __id = int
    __nome = str

    def __init__(self, id, nome):
        self.setId(id)
        self.setNome(nome)
    
    def __str__(self):
        return f"ID: {self.__id:03d} - Nome: {self.__nome}"

    # --------- SETTERS ---------
    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome

    # --------- GETTERS ---------
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

class Produto:
    __id = int
    __descricao = str
    __preco = float
    __estoque = int
    __categoria = Categoria 

    def __init__(self, id, descricao, preco, estoque, categoria):
        self.setId(id)
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setCategoria(categoria)
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.__id:03d}\n"
        texto += f"Descrição: {self.__descricao}\n"
        texto += f"Preço: R$ {self.__preco:0.2f}\n"
        texto += f"Estoque: {self.__estoque}\n"
        texto += f"Categoria: {self.__categoria.getNome()}"
        return texto


    # --------- SETTERS ---------
    def setId(self, id):
        self.__id = id

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setPreco(self, preco):
        self.__preco = preco

    def setEstoque(self, estoque):
        self.__estoque = estoque

    def setCategoria(self, categoria):
        self.__categoria = categoria

    # --------- GETTERS ---------
    def getId(self):
        return self.__id

    def getDescricao(self):
        return self.__descricao

    def getPreco(self):
        return self.__preco

    def getEstoque(self):
        return self.__estoque

    def getCategoria(self):
        return self.__categoria

class Venda:
    __id = int
    __data = datetime
    __carrinho = bool
    __total = float
    __cliente = Cliente
    __produtos = []

    def __init__(self, id: int, data: datetime, carrinho: bool, total: float, cliente: Cliente):
        self.setId(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setTotal(total)
        self.setCliente(cliente)
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.__id:03d}\n"
        texto += f"Data da venda: {self.__data.strftime("%d/%m/%Y")}\n"
        texto += f"Carrinho: {self.__carrinho}\n"
        texto += f"Total: R$ {self.__total:0.2f}\n"
        texto += f"Cliente: {self.__cliente.getNome()}\n"
        texto += "Produtos: \n"
        for p in self.__produtos:
            texto += f" - {p.getProduto().getDescricao()}\n"

        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.__id = id

    def setData(self, data):
        self.__data = data

    def setCarrinho(self, carrinho):
        self.__carrinho = carrinho

    def setTotal(self, total):
        self.__total = total

    def setCliente(self, cliente):
        self.__cliente = cliente
    
    def setProdutos(self, prod):
        self.__produtos.append(prod)

    # --------- GETTERS ---------
    def getId(self):
        return self.__id

    def getData(self):
        return self.__data

    def getCarrinho(self):
        return self.__carrinho

    def getTotal(self):
        return self.__total

    def getCliente(self):
        return self.__cliente

    def getProdutos(self):
        return self.__produtos

class VendaItem:
    __id = int
    __qtd = int
    __preco = float
    __venda = Venda
    __produto = Produto

    def __init__(self, id: int, qtd: int, preco: float, venda: Venda, produto: Produto):
        self.setId(id)
        self.setQtd(qtd)
        self.setPreco(preco)
        self.setVenda(venda)
        self.setProduto(produto)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.__id:03d}\n"
        texto += f"Produto: {self.__produto.getDescricao()}\n"
        texto += f"Quantidade: {self.__qtd}\n"
        texto += f"Preço Unitário: R$ {self.__preco:0.2f}\n"
        texto += f"Subtotal: R$ {self.__qtd * self.__preco:0.2f}"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.__id = id

    def setQtd(self, qtd):
        self.__qtd = qtd

    def setPreco(self, preco):
        self.__preco = preco

    def setVenda(self, venda):
        self.__venda = venda

    def setProduto(self, produto):
        self.__produto = produto

    # --------- GETTERS ---------
    def getId(self):
        return self.__id

    def getQtd(self):
        return self.__qtd

    def getPreco(self):
        return self.__preco

    def getVenda(self):
        return self.__venda

    def getProduto(self):
        return self.__produto




