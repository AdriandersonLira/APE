n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# -- algoritmo de euclides -- #

def mdc(n1,n2):
    if n1%n2==0:
        return n2
    return mdc(n2, n1%n2)

print(mdc(n1,n2))

# ---------- FIM ----------- #

num = n1
while n1%num != 0 or n2%num != 0:
    num -= 1

print(f'O mdc de {n1} e {n2} é {num}')