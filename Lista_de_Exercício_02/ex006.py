v1 = float(input())
c = int(v1)
c100 = c//100
c50 = (c%100)//50
c20 = ((c%100)%50)//20
c10 = (((c%100)%50)%20)//10
c5  = ((((c%100)%50)%20)%10)//5
c2  = (((((c%100)%50)%20)%10)%5)//2
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(c100))
print('{} nota(s) de R$ 50.00'.format(c50))
print('{} nota(s) de R$ 20.00'.format(c20))
print('{} nota(s) de R$ 10.00'.format(c10))
print('{} nota(s) de R$ 5.00'.format(c5))
print('{} nota(s) de R$ 2.00'.format(c2))
m1 = ((((((c%100)%50)%20)%10)%5)%2)
m = round((v1-c)*100)
m50 = m//50
m25 = (m%50)//25
m10 = ((m%50)%25)//10
m05 = (((m%50)%25)%10)//5
m01 = ((((m%50)%25)%10)%5)
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(m1))
print('{} moeda(s) de R$ 0.50'.format(m50))
print('{} moeda(s) de R$ 0.25'.format(m25))
print('{} moeda(s) de R$ 0.10'.format(m10))
print('{} moeda(s) de R$ 0.05'.format(m05))
print('{} moeda(s) de R$ 0.01'.format(m01))