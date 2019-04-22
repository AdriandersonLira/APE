n = int(input('Digite um número: '))
antes = 0
depois = 1
print('0 1',end=' ')
for i in range(n-2):
    print(antes + depois, end=' ')
    antes = depois
    depois = antes + depois

