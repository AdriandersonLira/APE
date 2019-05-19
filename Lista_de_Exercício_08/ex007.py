candidato = list()
lista = list()

for i in range(4000):
    matricula = int(input('Digite a matricula: '))
    quant_acertos = int(input('Quantidade de acertos: '))
    quant_erros = int(input('Quantidade de erros: '))
    quant_nao_respondida = int(input('Quantidade não respondida: '))
    # ---- add variaveis recebidas de cada candidato ---- #
    candidato.append(matricula)
    candidato.append(quant_acertos)
    candidato.append(quant_erros)
    candidato.append(quant_nao_respondida)
    # ---- verificando se a nota dele teve no mínimo 50% de acertos ---- #
    if candidato[1] >= candidato[2]:
        lista.append(candidato)
    canditado = list()

for i in lista:
    print(f'Matricula: {i[0]}')
    print(f'Quantidade de acertos: {i[1]}')
    print(f'Quantidade de erros: {i[2]}')
    print(f'Quantidade não respondida: {i[3]}')
