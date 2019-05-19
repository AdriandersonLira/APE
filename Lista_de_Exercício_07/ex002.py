n = int(input('Digite o tamanho do seu vetor: '))
vetor = list()

for i in range(n):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

print(vetor)
print(vetor[::-1])