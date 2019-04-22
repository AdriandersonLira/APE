n = int(input('Digite um número: '))
cont = 0
for i in range(1, n+1):
    if n%i==0:
        cont += 1
result = 'é primo' if cont == 2 else 'não é primo'
print(f'{n} {result}')
