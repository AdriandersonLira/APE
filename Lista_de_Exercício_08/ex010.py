from random import randint
vetor = list()

for i in range(10):
    vetor.append(randint(0,99))

for i in range(len(vetor)):
    for j in range(len(vetor)): 
        if vetor[i] > vetor[j]: vetor[i], vetor[j] = vetor[j], vetor[i]

print(vetor)