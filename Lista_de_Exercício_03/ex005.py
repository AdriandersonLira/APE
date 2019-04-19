nome = input()
saldo = float(input())
if 201 <= saldo <= 400:
    credito = (saldo*20)/100
elif 401 <= saldo <= 600:
    credito = (saldo*30)/100
elif saldo >= 601:
    credito = (saldo*40)/100
print(f'Cliente: {nome}\nSaldo Médio: {saldo}\nValor Credito: {credito}')