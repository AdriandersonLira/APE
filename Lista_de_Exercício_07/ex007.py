lista = []
cont = 0

while cont < 6:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        cont += 1
    else:
      print('Esse número já existe na lista...')

for i in lista:
    print(i, end=' ')