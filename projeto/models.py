from datetime import datetime
import re


class Cliente:
    def __init__(
        self,
        id: int,
        nome: str,
        email: str,
        senha: str,
        telef: str,
        is_admin: bool = False,
    ):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setTelefone(telef)
        self.setSenha(senha)
        self.setIsAdmin(is_admin)

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
        if ("@" not in email) and ("admin" not in email):
            raise ValueError("Email inválido")
        self.email = email

    def setTelefone(self, telefone):

        pattern = r"^\(\d{2}\)\s9\d{4}-\d{4}$"
        if not (re.match(pattern, telefone)):
            raise ValueError("Telefone inválido")

        self.telefone = telefone

    def setSenha(self, senha):
        self.senha = senha

    def setIsAdmin(self, is_admin):
        self.is_admin = is_admin

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

    def getIsAdmin(self):
        return self.is_admin

    # ---------- JSON -----------
    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "telefone": self.telefone,
        }

    def from_json(dic):
        return Cliente(
            dic["id"], dic["nome"], dic["email"], dic["senha"], dic["telefone"]
        )


class Categoria:
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
        return {"id": self.id, "nome": self.nome}

    def from_json(dic):
        return Categoria(dic["id"], dic["nome"])


class Produto:
    def __init__(
        self, id: int, descricao: str, preco: float, estoque: int, categoria_id: int
    ):
        self.setId(id)
        self.setDescricao(descricao)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setCategoria(categoria_id)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d} - {self.descricao}"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        self.id = id

    def setDescricao(self, descricao):
        self.descricao = descricao

    def setPreco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        self.preco = preco

    def setEstoque(self, estoque):
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo")
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
            "categoria": self.categoria_id,
        }

    def from_json(dic):
        return Produto(
            id=dic["id"],
            descricao=dic["descricao"],
            preco=dic["preco"],
            estoque=dic["estoque"],
            categoria_id=dic["categoria"],
        )


class Venda:
    def __init__(self, id: int, data: datetime, carrinho: bool, cliente: int):
        self.setId(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setCliente(cliente)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Data da venda: {self.data.strftime('%d/%m/%Y')}\n"
        texto += f"Carrinho: {self.carrinho}\n"
        texto += f"Cliente: {self.cliente}\n"
        return texto

    # --------- SETTERS ---------er
    def setId(self, id):
        self.id = id

    def setData(self, data):
        if data > datetime.now():
            raise ValueError("Data inválida")
        self.data = data

    def setCarrinho(self, carrinho):
        if not (isinstance(carrinho, bool)):
            raise ValueError("O carrinho deve ser um booleano")
        self.carrinho = carrinho

    def setCliente(self, cliente):
        if isinstance(cliente, str):
            raise ValueError("O ID não pode ser uma string")
        self.cliente = cliente

    # --------- GETTERS ---------
    def getId(self):
        return self.id

    def getData(self):
        return self.data

    def getCarrinho(self):
        return self.carrinho

    def getCliente(self):
        return self.cliente

    # ---------- JSON -----------
    def to_json(self):
        return {
            "id": self.id,
            "data": self.data.strftime("%d/%m/%Y"),
            "carrinho": self.carrinho,
            "cliente": self.cliente,
        }

    def from_json(dic):
        venda = Venda(
            id=dic["id"],
            data=datetime.strptime(dic["data"], "%d/%m/%Y"),
            carrinho=dic["carrinho"],
            cliente=dic["cliente"],
        )

        return venda


class VendaItem:
    def __init__(self, id: int, qtd: int, venda_id: int, produto_id: int, preco: float):
        self.setId(id)
        self.setQtd(qtd)
        self.setVenda(venda_id)
        self.setProduto(produto_id)
        self.setPreco(preco)

    def __str__(self):
        texto = ""
        texto += f"ID: {self.id:03d}\n"
        texto += f"Venda: {self.venda_id}\n"
        texto += f"Produto: {self.produto_id}\n"
        texto += f"Quantidade: {self.qtd}\n"
        texto += f"Preço Unitário: R$ {self.preco:0.2f}\n"
        texto += f"Subtotal: R$ {self.preco * self.qtd:0.2f}\n"
        return texto

    # --------- SETTERS ---------
    def setId(self, id):
        if isinstance(id, str):
            raise ValueError("O ID não pode ser uma string")
        self.id = id

    def setQtd(self, qtd):
        if qtd < 0:
            raise ValueError("A quantidade não pode ser negativa")
        self.qtd = qtd

    def setPreco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        self.preco = preco

    def setVenda(self, venda_id):
        if isinstance(venda_id, str):
            raise ValueError("O ID não pode ser uma string")
        self.venda_id = venda_id

    def setProduto(self, produto_id):
        if isinstance(produto_id, str):
            raise ValueError("O ID não pode ser uma string")
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
            "qtd": self.qtd,
        }

    def from_json(dic):
        return VendaItem(
            id=dic["id"],
            qtd=dic["qtd"],
            venda_id=dic["venda_id"],
            produto_id=dic["produto_id"],
            preco=dic["preco"],
        )


class Endereco:
    def __init__(
        self,
        id: int,
        cli: int,
        log: str,
        num: str,
        com: str,
        bai: str,
        cid: str,
        est: str,
        cep: str,
    ):
        self.setId(id)
        self.setCliente(cli)
        self.setLogradouro(log)
        self.setNumero(num)
        self.setComplemento(com)
        self.setBairro(bai)
        self.setCidade(cid)
        self.setEstado(est)
        self.setCEP(cep)

    # --- SETTERS ---
    def setId(self, id):
        self.id = id

    def setCliente(self, cli: int):
        self.cliente = cli

    def setLogradouro(self, log: str):
        self.logradouro = log

    def setNumero(self, num: int):
        self.numero = num

    def setComplemento(self, com: str):
        self.complemento = com

    def setBairro(self, bai: str):
        self.bairro = bai

    def setCidade(self, cid: str):
        self.cidade = cid

    def setEstado(self, est: str):
        self.estado = est

    def setCEP(self, cep: str):
        self.cep = cep

    # --- GETTERS ---

    def getId(self) -> int:
        return self.id

    def getCliente(self) -> int:
        return self.cliente

    def getLogradouro(self) -> str:
        return self.logradouro

    def getNumero(self) -> int:
        return self.numero

    def getComplemento(self) -> str:
        return self.complemento

    def getBairro(self) -> str:
        return self.bairro

    def getCidade(self) -> str:
        return self.cidade

    def getEstado(self) -> str:
        return self.estado

    def getCEP(self) -> str:
        return self.cep

    # --- JSON ---

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "cliente": self.cliente,
            "logradouro": self.logradouro,
            "numero": self.numero,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "cep": self.cep,
        }

    def from_json(dic):
        endereco = Endereco(
            id=dic["id"],
            cliente=dic["cliente"],
            logradouro=dic["logradouro"],
            numero=dic["numero"],
            complemento=dic["complemento"],
            bairro=dic["bairro"],
            cidade=dic["cidade"],
            estado=dic["estado"],
            cep=dic["cep"],
        )

        return endereco
