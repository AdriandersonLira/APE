while True:
    matricula = int(input('Digite a matricula do Aluno: '))
    if matricula == 0:
        break
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    media = (nota1+nota2)/2
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    print('Matricula: {}, Nome: {}, Média: {}, Situação: {}'.format(matricula, nome, media, situacao))
