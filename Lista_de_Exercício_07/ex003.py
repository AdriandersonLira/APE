n = int(input('Digite o tamanho do seu vetor: '))
vetor = list()

for i in range(n):
    a = int(input('Digite um número; '))
    vetor.append(a)

min_vetor = float('Inf')
max_vetor = float('-Inf')
for i in vetor:
    min_vetor = i if i < min_vetor else min_vetor
    max_vetor = i if i > max_vetor else max_vetor

print(f'max da lista: {max_vetor}')
print(f'min da lista: {min_vetor}')
