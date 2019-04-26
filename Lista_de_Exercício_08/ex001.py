n = int(input("Tamanho do vetor: "))
A = []
for i in range(n):
    A.append(int(input("Digite um número: ")))

k = int(input("Valor ao qual deseja multplicar os elementos do vetor: "))
B = []
for i in A:
    B.append(i * k)

print("A: ", A)
print("B: ", B)
