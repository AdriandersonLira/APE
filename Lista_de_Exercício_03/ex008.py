matricula = int(input('Matricula do aluno: '))
n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a nota: '))
n3 = float(input('Digite a nota: '))
media_exe = int(input('Informe a média dos exercícios: '))
media_apr = ( n1 + ( n2 * 2 ) + ( n3 * 3 ) + media_exe) / 7
if media_apr >= 9:
    conceito = 'A'
elif 7.5 >= media_apr < 9:
    conceito = 'B'
elif 6 >= media_apr < 7.5:
    conceito = 'C'
elif 4 >= media_apr < 6:
    conceito = 'D'
elif media_apr < 4:
    conceito = 'E'

situacao = 'APROVADO' if conceito == 'A' or conceito == 'B' or conceito == 'C' else 'REPROVADO'

print(f'Matricula: {matricula}\n\
        MA: {media_apr}\n\
        Conceito: {conceito}\n\
        Situação: {situacao}')
