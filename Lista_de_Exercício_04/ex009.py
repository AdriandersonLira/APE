from math import sqrt
a = int(input('Digite o número de a da sua equação: '))
b = int(input('Digite o número de b da sua equação: '))
c = int(input('Digite o número de c da sua equação: '))
delta = b**2 - (4 * a * c)
if delta < 0:
    print('Não existem as raízes da equação.')
else:
    x1 = (-b + (sqrt(delta)) ) / (2*a)
    x2 = (-b - (sqrt(delta)) ) / (2*a)
    print(f'x1: {x1}\nx2: {x2}')