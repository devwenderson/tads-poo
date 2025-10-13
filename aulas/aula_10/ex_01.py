from datetime import datetime
data1 = datetime(2025, 10, 10, 9, 41)
data2 = datetime.now()

print(f"Hora digitada pelo usuário: {data1}")
print(f"Data automática: {data2}")

data3 = datetime.strptime("26/05/2025 09:34", "%d/%m/%Y %H:%M")
print(f"Hora digitada pelo usuário: {data3}")
print(data3.date())
print(data3.weekday()) # 0 = Segunda-feira
