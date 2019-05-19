lista = []; cont = 0

for i in range(20):
    n = int(input('Digite um número: '))
    lista.append(n)

media = sum(lista)/len(lista)

for i in lista:
  if i < media:
    cont += 1

print(f'Os quantidade de números abaixo da média são: {cont}')
