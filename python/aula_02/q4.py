data = input("Digite uma da no formato dd/mm/aaaa: ")
data_in_list = data.split("/")

dia = int(data_in_list[0])
mes = int(data_in_list[1])
ano = int(data_in_list[2])
mensagem = "Data válida"

meses_com_31 = [1, 3, 5, 7, 8, 10, 12]
meses_com_30 = [4, 6, 9, 11]
meses_com_29 = [2]

if ano < 1900 or ano > 2100:
    mensagem = "A data informada não é válida"

if mes < 1 or mes > 12:
    mensagem = "A data informada não é válida"

if mes in meses_com_31 and dia > 31:
    mensagem = "A data informada não é válida"
elif mes in meses_com_30 and dia > 30:
    mensagem = "A data informada não é válida"
elif mes in meses_com_29 and dia > 29:
    mensagem = "A data informada não é válida"
        
print(f"{mensagem}")