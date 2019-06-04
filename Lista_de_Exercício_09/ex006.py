matriz = list()

for i in range(3):
    matriz.append(list())
    for j in range(3):
        matriz[i].append(int(input(f'Digite um número para ser add em matriz[{i}][{j}]: ')))

for i in matriz: print(i)

soma_lin = 0
print('a)A soma dos elementos de cada linha;')
for i in matriz:
    soma_lin = sum(i)
    print(f' {soma_lin}')
    soma_lin = 0

soma_col = 0
print('b)A soma dos elementos de cada coluna')

soma_all = 0
soma_pri = 0
soma_sec = 0
for i in range(3):
    for j in range(3):
        soma_col += matriz[j][i]
        soma_all += matriz[i][j]
    soma_pri += matriz[i][i]
    soma_sec += matriz[i][2-i]
    print(f' {soma_col}')
    soma_col = 0


print(f'c)A soma dos elementos da diagonal principal da matriz;\n {soma_pri}')
print(f'd)A soma dos elementos da diagonal secundária da matriz;\n {soma_sec}')
print(f'e)A soma de todos os elementos da matriz.\n {soma_all}')