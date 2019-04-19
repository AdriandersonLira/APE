n = int(input())
if n == 0 or n == 1:
    print('1')
else:
    cont = 1
    for i in range(1,n+1):
        cont *= i
    print(cont)

