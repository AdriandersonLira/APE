gabarito = list()
respostas = list()

for i in range(10):
    n = int(input(f'Digite a resposta CORRETA da questão {i+1}: '))
    gabarito.append(n)

for i in range(10):
    n = int(input(f'Digite a resposta DO ALUNO da questão {i+1}: '))
    respostas.append(n)

cont = 0
for i in range(10):
    cont += 1 if gabarito[i] == respostas[i] else 0

print(f'A quantidade de Respostas corretas é igual a {cont}')

