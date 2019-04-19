n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2 and n1 > n3:
    n = n1
elif n2 > n1 and n2 > n3:
    n = n2
elif n3 > n1 and n3 > n2:
    n = n3
print(f'{n} é o maior')