n = int(input('Digite o número para o tamanho da matriz quadrada: '))
matriz = list()

for i in range(n):
    matriz.append(list())
    for j in range(n):
        matriz[i].append(int(input(f'Digite um número para ser add em matriz[{i}][{j}]: ')))

# --- verificando linhas ---- #

aux = 0
ver = True

for i in range(n):
    cont = sum(matriz[i])
    if i >= 1:
        if cont != aux: ver = False; break
    else: 
        aux = cont

# --- verificando colunas ---- #

if ver:
    cont = 0

    for i in range(n):
        for j in range(n):
            cont += matriz[j][i]
        if cont != aux: ver = False; break
        cont = 0

# --- verificando diagonal principal ---- #

if ver:
    for i in range(n):
        for j in range(n):
            cont += matriz[j][j]
        if cont != aux: ver = False; break
        cont = 0

# --- verificando diagonal secundária ---- #

if ver:
    for i in range(n):
        for j in range(n-1, -1, -1):
            cont += matriz[(n-1)-j][j]
        if cont != aux: ver = False; break
        cont = 0


ok = '' if ver else 'não'
for i in matriz: print(i)
print(f'Essa matriz {ok} é uma matriz mágica.')
