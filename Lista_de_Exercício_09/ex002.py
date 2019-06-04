n = int(input('Digite o tamanho da sua matriz quadrada: '))
matriz = list()

for i in range(n):
    matriz.append(list())
    for j in range(n):
        number = int(input(f'Digite um número para add na posicao matriz[{i}][{j}]: '))
        matriz[i].append(number)

for i in matriz: print(i)

print()
for i in range(n):
    for j in range(n):
        if i == j:
            print(matriz[i][j])

