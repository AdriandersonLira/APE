sorteio = [ 6, 7, 13, 14, 26 ]
lista = list()
for i in range(60):
    cont_oito = 8
    while cont_oito != 0:
        numero = int(input('Digite o número: '))
        if numero not in range(1,81) or numero in lista:
            print('Aposta inválida, digite um número dentro do intervalo de [1, 80]')
        else:
            cont_oito -= 1
            lista.append(numero)
    cont = 0
    for i in lista:
        for j in sorteio:
            if i == j:
                cont += 1
    lista = list()
    
    print(f'A quantidade de acertos foi: {cont}')
        