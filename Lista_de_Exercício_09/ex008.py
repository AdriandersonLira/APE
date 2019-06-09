matriz = list()

# matriz 4 x 6 -- pedindo valores ao user -- 
'''
# letra A)

for i in range(4):
    matriz.append(list())
    for j in range(6):
        matriz[i].append( int(input('informe o número a ser inserido na matriz: ')) )
'''
# matriz pronta --

matriz = [[204,223,230,257,290,322], [195,192,198,203,208,228], [220,222,217,231,245,280], [254,262,279,284,296,330]]

print('# letra B)')

ano = 2012
ver = 0 

for i in range(6):
    for j in range(4):
        if matriz[j][j] > ver:
            x = j+1
        ver = matriz[j][j]
    print(f'No ano {ano} o fabricante {x} vendeu mais')
    ano += 1

print('\n# letra C)\n')

cont = 0

for i in range(6):
    ver = cont
    cont = 0
    for j in range(4):
        cont += matriz[j][i]
    if cont > ver:
        ano = 2010 + i + 2

print(f'O ano que houve mais volume de Vendas foi: {ano}')
    


print('\n# letra D)\n')

for i in matriz:
    print('Média de Vendas de cada fabricante: {:.2f}'.format(sum(i)/len(i)))
