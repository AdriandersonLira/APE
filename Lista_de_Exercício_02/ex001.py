A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))
At = (A*C)/2
Ac = 3.14159*C**2
Atr= ((A+B)*C)/2
Aq = B**2
Ar = A*B
print('a. a área do triângulo retângulo que tem {} por base e {} por altura é = {}'.format(A,C,At))
print('b. a área do círculo de raio {}. (pi = 3.14159) é = {}'.format(C,Ac))
print('c. a área do trapézio que tem {} e {} por bases e {} por altura.'.format(A,B,C,Atr))
print('d. a área do quadrado que tem lado {} é = {}'.format(B,Aq))
print('e. a área do retângulo que tem lados {} e {} é = {}'.format(A,B,Ar))
