'''
a divisão entre eles possui resto igual a zero, 
dizemos que os números são múltiplos. Observe:

28 é múltiplo de 14, pois 28 : 14 = 2 e resto 0
55 é divisível por 5, pois 55:5 = 11 e resto 0.
81 é divisível por 9, pois 81:9 = 9 e resto 0
121 é divisível por 11, pois 121:11 = 11 e resto 0
'''

n = int(input())
for i in range(1,51):
    if i%n==0:
        print(i, end=' ')
