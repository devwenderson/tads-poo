import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

a = Cliente(1, "Douglas Crockford")
b = Cliente(2, "Jon Bosak")
c = Cliente(3, "William Henry Gates III")

clientes = [a, b, c]

arquivo = open("./aulas/aula_12/clientes.json", mode="w")
json.dump(clientes, arquivo, default=vars, indent=4)
arquivo.close() # sempre fechar arquivos depois de usar