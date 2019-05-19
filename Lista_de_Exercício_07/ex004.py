vetor = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]

for i in range(20):
    vetor.append(i)

print(vetor)

K = int(input('Digite um número presente no vetor: '))

cont = 0
for i in vetor:
    cont += 1 if i == K else 0

print(f'A quantidade de vezes do número {K} no vetor é {cont}')
