lista = []

for i in range(6):
    n = int(input('Digite um número: '))
    lista.append(n)

if len(set(lista)) == len(lista): print('Não existe repetição entre os números lidos')
else: print('Existe repetição entre os números lidos')