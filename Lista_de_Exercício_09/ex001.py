# ---- definição de funções ---- #

def definir_matriz(matriz):
    for i in range(2):
        matriz.append(list())
    
    return matriz

def inserir_numeros(matriz):
    for i in range(2):
        for j in range(3):
            n = int(input(f'Digite um número para ocuar na posição matriz[{i}][{j}]: '))
            matriz[i].append(n)
    
    return matriz

def printar(matriz):
    for i in matriz: print(i)
    print()

# ---- programa ---- #

matriz_1 = list()
matriz_2 = list()
matriz_s = list()

matriz_1 = definir_matriz(matriz_1)
matriz_2 = definir_matriz(matriz_2)
matriz_s = definir_matriz(matriz_s)

matriz_1 = inserir_numeros(matriz_1)
matriz_2 = inserir_numeros(matriz_2)

for i in range(2):
    for j in range(3):
        matriz_s[i].append(matriz_1[i][j] + matriz_2[i][j])

printar(matriz_1)
printar(matriz_2)
printar(matriz_s)
