n = int(input('Digite um número: '))
x = int(input('Digite um número: '))
y = int(input('Digite um número: '))

print(f'Os múltiplos de {n} entre {x} e {y} são: \n')
for i in range(x,y):
    if i%n==0: print(i, end=' ')