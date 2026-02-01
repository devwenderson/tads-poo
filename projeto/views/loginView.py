from views.clienteView import ClienteView

class LoginView:
    def autenticar(email, senha):
        clientes = ClienteView.cliente_listar()
        for c in clientes:
            if c.getEmail() == email and c.getSenha() == senha:
                return {"id": c.getId(), "nome": c.getNome()}      
        return None

    def criar_admin():
        clientes = ClienteView.cliente_listar()
        if clientes:
            for c in clientes:
                if c.getEmail() == "admin": 
                    return True
            ClienteView.cliente_inserir("admin", "admin", "admin", "(84) 91111-1111")