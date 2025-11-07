from models import Cliente, Categoria, Produto, Venda, VendaItem
from dao_classes import ClienteDAO, CategoriaDAO, ProdutoDAO, VendaDAO, VendaItemDAO
from views import View

class UI:
    __usuario = None
    
    @staticmethod
    def menu_visitante():
        opcoes = ""
        opcoes += "1 - Entrar no sistema\n"
        opcoes += "2 - Criar conta\n"
        opcoes += "9 - Sair do sistema\n"
        print(opcoes)
        
        op = int(input("Informe uma opção: "))
        if op == 1: UI.visitante_entrar()
        elif op == 2: UI.visitante_criar_conta()
        
        return op
    
    @classmethod
    def visitante_entrar(cls):
        email = input("Email: ")
        senha = input("Senha: ")
        cls.__usuario = View.autenticar(email, senha)
        if cls.__usuario == None: print("\n===== Email ou senha inválidos =====\n")
    
    @staticmethod
    def visitante_criar_conta():
        UI.cliente_inserir()
    
    @staticmethod
    def menu_admin():
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
        opcoes += "14 - Listar vendas\n"
        opcoes += "===========================\n"
        opcoes += "15 - Sair\n"
        print(opcoes)
        
        op = int(input("Informe uma opção: "))
        if op == 1: UI.inserir_cliente()
        elif op == 2: UI.listar_cliente()
        elif op == 3: UI.atualizar_cliente()
        elif op == 4: UI.excluir_cliente()
        elif op == 5: UI.inserir_categoria()
        elif op == 6: UI.listar_categoria()
        elif op == 7: UI.atualizar_categoria()
        elif op == 8: UI.excluir_categoria()
        elif op == 9: UI.inserir_produto()
        elif op == 10: UI.listar_produto()
        elif op == 11: UI.atualizar_produto()
        elif op == 12: UI.excluir_produto()
        elif op == 13: UI.produto_reajustar()
        elif op == 14: UI.venda_listar()
        elif op == 15: UI.usuario_sair()
    
    @staticmethod
    def menu_cliente():
        opcoes = ""
        opcoes += "1 - Listar produtos\n"
        opcoes += "2 - Inserir produto no carrinho\n"
        opcoes += "3 - Visualizar carrinho\n"
        opcoes += "4 - Comprar do carrinho\n"
        opcoes += "5 - Listar minhas compras\n"
        opcoes += "9 - Sair\n"
        print(opcoes)
        
        op = int(input("Informe uma opção: "))
        if op == 1: pass
        elif op == 2: pass
        elif op == 3: pass
        elif op == 4: pass
        elif op == 5: pass
        elif op == 9: UI.usuario_sair()
    
    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None
    
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__usuario == None:
                op = UI.menu_visitante()
            else:
                admin = cls.__usuario["nome"] == "admin"
                print(f"\n{'='*30}")
                print("Comércio eletrônico 2025")
                print(f"Bem-vindo(a), {cls.__usuario["nome"]}")
                print(f"{'='*30}\n")

                if admin: UI.menu_admin()
                else: UI.menu_cliente()
        
        print("\n===== Saindo do sistema... =====\n")
    
    @staticmethod
    def main():
        View.criar_admin()
        UI.menu()

    # --------- Clientes ---------
    @staticmethod
    def cliente_inserir():
        print("\n----- INSERIR CLIENTE -----\n")
        
        nome = input("Nome: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")

        View.cliente_inserir(nome, email, senha, telefone)
        print("Cliente cadastrado com sucesso\n")

    @staticmethod
    def cliente_listar():
        print("\n----- LISTAR CLIENTES -----")
        clientes = View.cliente_listar()
        for cli in clientes:
            print(cli)

    @staticmethod
    def cliente_atualizar():
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
    def cliente_excluir():
        print("\n----- EXCLUIR CLIENTE -----\n")
        UI.listar_cliente()

        print("Escolha o ID para excluir")
        id = int(input("ID: "))
        View.cliente_excluir(id)
        print("Cliente excluído com sucesso\n")



    # --------- Categorias ---------
    @staticmethod
    def categoria_inserir():
        print("\n----- INSERIR CATEGORIA -----\n")
        nome = input("Nome da categoria: ")
        View.categoria_inserir(nome)
        print("Categoria cadastrada com sucesso\n")
        

    @staticmethod
    def categoria_listar():
        print("\n----- LISTAR CATEGORIAS -----\n")
        categorias = View.categoria_listar()
        for c in categorias:
            print(c)
        
    @staticmethod
    def categoria_atualizar():
        print("\n----- ATUALIZAR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser atualizado: "))
        nome = input("Nome da categoria: ")
        View.categoria_atualizar(id, nome)
        print("\n----- CATEGORIA ATUALIZADA! -----\n")

    @staticmethod
    def categoria_excluir():
        print("\n----- EXCLUIR CATEGORIA -----\n")
        UI.listar_categoria()
        id = int(input("Insira o ID a ser excluído: "))
        View.categoria_excluir(id)



    # --------- Produtos ---------
    @staticmethod
    def produto_inserir():
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
    def produto_listar():
        print("\n----- LISTAR PRODUTOS -----\n")
        produtos = View.produto_listar()
        for prod in produtos:
            print(prod)
        
    @staticmethod
    def produto_atualizar():
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
    def produto_excluir():
        print("\n----- EXCLUIR PRODUTO -----\n")
        UI.listar_produto()
        id = int(input("Informe o ID a ser excluído: "))
        View.produto_excluir(id)
    
    @staticmethod
    def produto_reajustar():
        print("\n----- REAJUSTAR PREÇO DOS PRODUTOS -----\n")
        percentual = int(input("Informe o percentual: "))
        View.produto_reajustar(percentual)
    
    
    
    # ===== VENDAS =====
    def venda_listar():
        print("\n----- LISTAR VENDAS -----\n")
        vendas = View.vendas_listar()
        for v in vendas:
            print(v)
        
        


UI.main()