lista = []

for i in range(6):
    n = int(input('Digite um número: '))
    lista.append(n)

lista.reverse()
for i in lista:
    print(i, end=' ')
