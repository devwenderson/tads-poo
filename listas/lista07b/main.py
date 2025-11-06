from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO
from views import View

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
        opcoes += "13 - Reajustar preços\n"
        opcoes += "===========================\n"
        opcoes += "14 - Sair\n"
        print(opcoes)
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 14:
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
                UI.produto_reajustar()
            elif op == 14:
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

        View.cliente_inserir(nome, email, telefone)
        print("Cliente cadastrado com sucesso\n")

    @staticmethod
    def listar_cliente():
        print("\n----- LISTAR CLIENTES -----")
        clientes = View.cliente_listar()
        for cli in clientes:
            print(cli)

    @staticmethod
    def atualizar_cliente():
        print("\n----- ATUALIZAR CLIENTE -----\n")
        try:
            UI.listar_cliente()
            
            print("Escolha o ID para atualizar")
            id = input("ID: ")
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")

            View.cliente_atualizar(id, nome, email, telefone)
            
            print("Cliente atualizado com sucesso\n")
        except:
            print("Algum dado está incorreto\n")

    @staticmethod
    def excluir_cliente():
        print("\n----- EXCLUIR CLIENTE -----\n")
        UI.listar_cliente()

        print("Escolha o ID para excluir")
        id = int(input("ID: "))
        View.cliente_excluir(id)
        print("Cliente excluído com sucesso\n")



    # --------- Categorias ---------
    @staticmethod
    def inserir_categoria():
        print("\n----- INSERIR CATEGORIA -----\n")
        nome = input("Nome da categoria: ")
        View.categoria_inserir(nome)
        print("Categoria cadastrada com sucesso\n")
        

    @staticmethod
    def listar_categoria():
        print("\n----- LISTAR CATEGORIAS -----\n")
        categorias = View.categoria_listar()
        for c in categorias:
            print(c)
        
    @staticmethod
    def atualizar_categoria():
        print("\n----- ATUALIZAR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser atualizado: "))
        nome = input("Nome da categoria: ")
        View.categoria_atualizar(id, nome)
        print("\n----- CATEGORIA ATUALIZADA! -----\n")

    @staticmethod
    def excluir_categoria():
        print("\n----- EXCLUIR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser excluído: "))
        View.categoria_excluir(id)



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
        View.produto_inserir(descricao, preco, estoque, categoria_id)
        print("\n----- PRODUTO CRIADO! -----\n")

        
    @staticmethod
    def listar_produto():
        print("\n----- LISTAR PRODUTOS -----\n")
        produtos = View.produto_listar()
        for prod in produtos:
            print(prod)
        
    @staticmethod
    def atualizar_produto():
        print("\n----- ATUALIZAR PRODUTO -----\n")
        UI.listar_produto()
        id = input("Informe o ID a ser atualizado: ")
        descricao = input("Descrição do produto: ")
        preco = input("Preço: ")
        estoque = input("Quant. em estoque: ")

        print("\n----- CATEGORIAS -----\n")
        UI.listar_categoria()
        print("\n----- ---------- -----\n")

        categoria_id = input("Informe o id da categoria: ")
        View.produto_atualizar(id, descricao, preco, estoque, categoria_id)

    @staticmethod
    def excluir_produto():
        print("\n----- EXCLUIR PRODUTO -----\n")
        UI.listar_produto()
        id = int(input("Informe o ID a ser excluído: "))
        View.produto_excluir(id)
    
    @staticmethod
    def produto_reajustar():
        print("\n----- REAJUSTAR PREÇO DOS PRODUTOS -----\n")
        percentual = int(input("Informe o percentual: "))
        View.produto_reajustar(percentual)


UI.main()