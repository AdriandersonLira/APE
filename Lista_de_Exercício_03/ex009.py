indice_de_poluicao = int(input())
if indice_de_poluicao <= 25:
    print('Índice de poluição aceitável')
elif 25 < indice_de_poluicao <= 39:
    print('As indústrias do 1° grupo são intimadas a suspenderem suas atividades.')
elif 40 <= indice_de_poluicao <= 49:
    print('As indústrias do 1° e 2° grupos são intimadas a suspenderem suas atividades.')
elif indice_de_poluicao >= 50:
    print('Todos os 3 grupos devem ser notificados a paralisarem suas atividades.')
