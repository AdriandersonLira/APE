maior = float('-inf')
menor = float('inf')
for i in range(5):
    n = int(input())
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
print('O maior número do conjunto de números digitados foi: {} e o menor foi: {}'.format(maior, menor))