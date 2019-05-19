lista_par = []
lista_impar = []

for i in range(10):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print('Números impares digitados: ', end='')
for i in lista_impar:
    print(i, end=' ')

print()
print('Números pares digitados: ', end='')
for i in lista_par:
    print(i, end=' ')