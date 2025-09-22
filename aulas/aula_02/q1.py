n = list(map(int, input().split()))
soma_pares = 0
soma_impares = 0

for i in n:
    if (i % 2 == 0):
        soma_pares = soma_pares + i
    elif (i % 2 != 0):
        soma_impares = soma_impares + i

print(f"Soma pares: {soma_pares}")
print(f"Soma ímpares: {soma_impares}")