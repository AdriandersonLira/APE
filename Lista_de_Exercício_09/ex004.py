n = int(input('Digite o tamanho da matriz: '))
matriz = list()

for i in range(n):
    matriz.append(list())
    for j in range(n):
        while True:
            num = int(input(f'Digite um número 1 ou 0 para add na posição matriz[{i}][{j}]: '))
            if num == 0 or num == 1:
                matriz[i].append(num)
                break
            else: print('Digite o número 1 ou 0...')

cont_line = 0
cont_colunm = 0
ver = True

for i in range(n):
    for j in range(n):
        if matriz[i][j] == 1: 
            cont_line += 1
        if matriz[j][i] == 1: 
            cont_colunm += 1
        if cont_line > 1 or cont_colunm > 1: 
            ver = False
            break
    if ver != True: 
        break
    cont_line = 0
    cont_colunm = 0

result = 'é' if ver else 'não é'

print(f'Está {result} uma matriz de permutação\n')

for i in matriz: print(i)