from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO

class UI:
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

    def main():
        op = 0
        while op != 13:
            op = UI.menu()

            if op == 1:
                UI.inserir_usuario()
            elif op == 2:
                UI.listar_usuario()
            elif op == 3:
                UI.atualizar_usuario()
            elif op == 4:
                UI.excluir_usuario()
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
    def inserir_usuario():
        print("----- INSERIR CLIENTE -----\n")
        
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        cliente = Cliente(0, nome, email, telefone)
        ClienteDAO.inserir(cliente)
        print("Cliente cadastrado com sucesso\n")


    @staticmethod
    def listar_usuario():
        print("----- LISTAR CLIENTES -----")
        clientes = ClienteDAO.listar()

    @staticmethod
    def atualizar_usuario():
        pass

    @staticmethod
    def excluir_usuario():
        pass

    # --------- Categorias ---------
    @staticmethod
    def inserir_categoria():
        pass

    @staticmethod
    def listar_categoria():
        pass

    @staticmethod
    def atualizar_categoria():
        pass

    @staticmethod
    def excluir_categoria():
        pass

    # --------- Produtos ---------
    @staticmethod
    def inserir_produto():
        pass

    @staticmethod
    def listar_produto():
        pass

    @staticmethod
    def atualizar_produto():
        pass

    @staticmethod
    def excluir_produto():
        pass

UI.main()