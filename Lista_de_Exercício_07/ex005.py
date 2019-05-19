vetor_A = list()
vetor_B = list()

for i in range(10):
    n = int(input('Digite um número: '))
    vetor_A.append(n)
    
for i in range(len(vetor_A)):
    vetor_B.append( vetor_A[i] * 2 if i%2 == 0  else vetor_A[i] * 3)

print(vetor_B)