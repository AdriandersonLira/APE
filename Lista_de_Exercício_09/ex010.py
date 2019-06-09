matriz = list()

# matriz 5 x 5 -- pedindo valores ao user -- 
'''
# letra A)

for i in range(5):
    matriz.append(list())
    for j in range(5):
        matriz[i].append( int(input('informe o número a ser inserido na matriz: ')) )
'''
# matriz pronta --

matriz = [[ '-', 15, 30, 5, 12 ], [ 15, '-', 10, 17, 28 ], [ 30, 10, '-', 3, 11 ], [ 5, 17, 3, '-', 80, ], [ 12, 28, 11, 80, '-' ]]
percurso = list(map(int, input('Informe o percuso: ').split(',')))

soma = 0
dist_perc = list()

for i in range(len(percurso)-1):
    dist_perc.append(matriz[percurso[i]-1][percurso[i+1]-1])
    soma += matriz[percurso[i]-1][percurso[i+1]-1]

dist_perc = ' + '.join(map(str, dist_perc))
percurso  = ', '.join(map(str, percurso))
print(f'dado o percurso {percurso} a distância percorrida é {dist_perc} = {soma}km.')
