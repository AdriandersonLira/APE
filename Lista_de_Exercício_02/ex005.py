v1 = int(input())
c100 = v1//100
r = v1%100
c50 = r//50
r = r%50
c20 = r//20
r = r%20
c10 = r//10
r = r%10
c5 = r//5
r = r%5
c2 = r//2
r = r%2
c1 = r
print(v1)
print('{} nota(s) de R$ 100,00'.format(c100))
print('{} nota(s) de R$ 50,00'.format(c50))
print('{} nota(s) de R$ 20,00'.format(c20))
print('{} nota(s) de R$ 10,00'.format(c10))
print('{} nota(s) de R$ 5,00'.format(c5))
print('{} nota(s) de R$ 2,00'.format(c2))
print('{} nota(s) de R$ 1,00'.format(c1))
