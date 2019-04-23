lista = []
for i in range(10): 
    n = int(input('Digite um número: '))
    lista.append(n)

lista.reverse()
for i in lista:
    print(i, end=' ')
