n = int(input('Digite o tamanho do seu vetor: '))
vetor_A = list()
vetor_B = list()

for i in range(n):
    numero = int(input('Digite um número: '))
    vetor_A.append(numero)

k = int(input('Digite um número: '))

for i in vetor_A:
    vetor_B.append(i*k)

print(vetor_A)
print(vetor_B)