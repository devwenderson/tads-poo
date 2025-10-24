from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO

class UI:
    @staticmethod
    def menu():
        opcoes = ""
        opcoes += "1 - Inserir Cliente\n"
        opcoes += "2 - Listar Cliente\n"
        opcoes += "3 - Atualizar Cliente\n"
        opcoes += "4 - Excluir Cliente\n"
        opcoes += "===========================\n"
        opcoes += "5 - Inserir Categoria\n"
        opcoes += "6 - Listar Categoria\n"
        opcoes += "7 - Atualizar Categoria\n"
        opcoes += "8 - Excluir Categoria\n"
        opcoes += "===========================\n"
        opcoes += "9 - Inserir Produto\n"
        opcoes += "10 - Listar Produto\n"
        opcoes += "11 - Atualizar Produto\n"
        opcoes += "12 - Excluir Produto\n"
        opcoes += "===========================\n"
        opcoes += "13 - Sair\n"
        print(opcoes)
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()

            if op == 1:
                UI.inserir_cliente()
            elif op == 2:
                UI.listar_cliente()
            elif op == 3:
                UI.atualizar_cliente()
            elif op == 4:
                UI.excluir_cliente()
            elif op == 5:
                UI.inserir_categoria()
            elif op == 6:
                UI.listar_categoria()
            elif op == 7:
                UI.atualizar_categoria()
            elif op == 8:
                UI.excluir_categoria()
            elif op == 9:
                UI.inserir_produto()
            elif op == 10:
                UI.listar_produto()
            elif op == 11:
                UI.atualizar_produto()
            elif op == 12:
                UI.excluir_produto()
            elif op == 13:
                print("Saindo do sistema...")
            else:
                print("Opção inválida!")

    # --------- Clientes ---------
    @staticmethod
    def inserir_cliente():
        print("\n----- INSERIR CLIENTE -----\n")
        
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        cliente = Cliente(0, nome, email, telefone)
        ClienteDAO.inserir(cliente)
        print("Cliente cadastrado com sucesso\n")

    @staticmethod
    def listar_cliente():
        print("\n----- LISTAR CLIENTES -----")
        clientes = ClienteDAO.listar()
        for cli in clientes:
            print(cli)

    @staticmethod
    def atualizar_cliente():
        print("\n----- ATUALIZAR CLIENTE -----\n")
        UI.listar_cliente()
        
        print("Escolha o ID para atualizar")
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        cliente = Cliente(id, nome, email, telefone)
        ClienteDAO.atualizar(cliente)
        print("Cliente atualizado com sucesso\n")

    @staticmethod
    def excluir_cliente():
        print("\n----- EXCLUIR CLIENTE -----\n")
        UI.listar_cliente()

        print("Escolha o ID para excluir")
        id = int(input("ID: "))
        cliente = Cliente(id, nome="", email="", telef="")
        ClienteDAO.excluir(cliente)
        print("Cliente excluído com sucesso\n")

    # --------- Categorias ---------
    @staticmethod
    def inserir_categoria():
        print("\n----- INSERIR CATEGORIA -----\n")
        nome = input("Nome da categoria: ")
        categoria = Categoria(0, nome)
        CategoriaDAO.inserir(categoria)
        print("Categoria cadastrada com sucesso\n")
        

    @staticmethod
    def listar_categoria():
        print("\n----- LISTAR CATEGORIAS -----\n")
        categorias = CategoriaDAO.listar()
        for c in categorias:
            print(c)
        

    @staticmethod
    def atualizar_categoria():
        print("\n----- ATUALIZAR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser atualizado: "))
        nome = input("Nome da categoria: ")
        categoria = Categoria(id, nome)
        CategoriaDAO.atualizar(categoria)

    @staticmethod
    def excluir_categoria():
        print("\n----- EXCLUIR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser excluído: "))
        categoria = Categoria(id, nome="")
        CategoriaDAO.excluir(categoria)

    # --------- Produtos ---------
    @staticmethod
    def inserir_produto():
        print("\n----- INSERIR PRODUTO -----\n")

        descricao = input("Descrição do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quant. em estoque: "))

        print("\n----- CATEGORIAS -----\n")
        UI.listar_categoria()
        print("\n----- ---------- -----\n")
        categoria_id = int(input("Informe o id da categoria: "))
        produto = Produto(0, descricao, preco, estoque, categoria_id)
        ProdutoDAO.inserir(produto)
        

    @staticmethod
    def listar_produto():
        print("\n----- LISTAR PRODUTOS -----\n")
        produtos = ProdutoDAO.listar()
        for prod in produtos:
            print(prod)
        
    @staticmethod
    def atualizar_produto():
        print("\n----- ATUALIZAR PRODUTO -----\n")
        UI.listar_produto()
        id = int(input("Informe o ID a ser atualizado: "))
        descricao = input("Descrição do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quant. em estoque: "))

        print("\n----- CATEGORIAS -----\n")
        UI.listar_categoria()
        print("\n----- ---------- -----\n")

        categoria_id = int(input("Informe o id da categoria: "))
        categoria = CategoriaDAO.busca_obj(categoria_id)
        produto = Produto(id, descricao, preco, estoque, categoria)

        ProdutoDAO.atualizar(produto)

    @staticmethod
    def excluir_produto():
        print("\n----- EXCLUIR PRODUTO -----\n")
        UI.listar_produto()
        id = int(input("Informe o ID a ser excluído: "))
        produto = Produto(id, descricao="", preco=0.0, estoque=0, categoria=None)
        ProdutoDAO.excluir(produto)

UI.main()