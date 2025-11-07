from datetime import datetime

class Cliente:
    id = int
    nome = str
    email = str
    telefone = str

    def __init__(self, id: int, nome: str, email: str, senha: str, telef: str):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setTelefone(telef)
        self.setSenha(senha)

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
    
    def setSenha(self, senha):
        self.senha = senha

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getTelefone(self):
        return self.telefone

    def getSenha(self):
        return self.senha
    
    # ---------- JSON -----------
    def to_json(self):
        return { "id": self.id,"nome": self.nome, "email": self.email, "senha": self.senha, "telefone": self.telefone }
    
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["senha"], dic["telefone"])

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

    # ---------- JSON -----------
    def to_json(self):
        return { "id": self.id, "nome": self.nome }
    
    def from_json(dic):
        return Categoria(dic["id"], dic["nome"])


class Produto:
    id = int
    descricao = str
    preco = float
    estoque = int
    categoria_id = int

    def __init__(self, id: int, descricao: str, preco: float, estoque: int, categoria_id: int):
        self.setId(id)
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setCategoria(categoria_id)
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Descrição: {self.descricao}\n"
        texto += f"Preço: R$ {self.preco:0.2f}\n"
        texto += f"Estoque: {self.estoque}\n"
        texto += f"Categoria: {self.categoria_id}\n"
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

    def setCategoria(self, categoria_id):
        self.categoria_id = categoria_id

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
        return self.categoria_id
    
    # ---------- JSON -----------
    def to_json(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "categoria": self.categoria_id
        }
    
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["categoria"])

class Venda:
    id = int
    data = datetime
    carrinho = bool
    cliente = int
    produtos = [int]

    def __init__(self, id: int, data: datetime, carrinho: bool, cliente: int):
        self.setId(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setCliente(cliente)
        self.produtos = []
    
    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Data da venda: {self.data.strftime('%d/%m/%Y')}\n"
        texto += f"Carrinho: {self.carrinho}\n"
        texto += f"Total: R$ {self.getTotal():0.2f}\n"
        texto += f"Cliente: {self.cliente}\n"
        texto += "Produtos: \n"
        for pro in self.produtos:
            texto += f" - {pro}\n"

        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setData(self, data):
        self.data = data

    def setCarrinho(self, carrinho):
        self.carrinho = carrinho

    def setCliente(self, cliente):
        self.cliente = cliente
    
    def setProdutos(self, prod_id):
        self.produtos.append(prod_id)

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getCarrinho(self):
        return self.carrinho

    def getTotal(self):
        total = 0
        for p in self.produtos:
            total += 0 # Precisa atualizar
        return total

    def getCliente(self):
        return self.cliente

    def getProdutos(self):
        return self.produtos
    
    # ---------- JSON -----------
    def to_json(self):
        return {
            "id": self.id,
            "data": self.data.strftime("%d/%m/%Y"),
            "carrinho": self.carrinho,
            "cliente": self.cliente,
            "produtos": self.produtos
        }
    
    def from_json(dic):
        venda = Venda(
            dic["id"],
            datetime.strptime(dic["data"], "%d/%m/%Y"),
            dic["carrinho"],
            dic["cliente"]
        )

        for pro in dic["produtos"]:
            venda.setProdutos(pro)
        
        return venda

class VendaItem:
    id = int
    qtd = int
    preco = float
    venda_id = int
    produto_id = int

    def __init__(self, id: int, qtd: int, venda_id: int, produto_id: int, preco: float):
        self.setId(id)
        self.setQtd(qtd)
        self.setVenda(venda_id)
        self.setProduto(produto_id)
        self.setPreco(preco)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Produto: {self.produto_id}\n"
        texto += f"Quantidade: {self.qtd}\n"
        texto += f"Preço Unitário: R$ {self.preco:0.2f}\n"
        texto += f"Subtotal: R$ {self.preco * self.qtd:0.2f}\n"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setQtd(self, qtd):
        self.qtd = qtd

    def setPreco(self, preco):
        self.preco = preco

    def setVenda(self, venda_id):
        self.venda_id = venda_id

    def setProduto(self, produto_id):
        self.produto_id = produto_id

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getQtd(self):
        return self.qtd

    def getPreco(self):
        return self.preco

    def getVenda(self):
        return self.venda_id

    def getProduto(self):
        return self.produto_id
    
    # ---------- JSON -----------
    def to_json(self):
        return {
            "id": self.id,
            "venda_id": self.venda_id,
            "produto_id": self.produto_id,
            "preco": self.preco,
            "qtd": self.qtd
        }

    def from_json(dic):
        return VendaItem(
            dic["id"],
            dic["venda_id"],
            dic["produto_id"],
            dic["qtd"],
            dic["preco"]
        )
    





