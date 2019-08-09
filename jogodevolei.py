print('Jogo de Vôlei até os 21 Pontos.')
equipe_a = 0
equipe_b = 0

while True: 
    saber = input('Equipe que pontuou: ').upper()

    if saber == 'A': equipe_a += 1
    elif saber == 'B': equipe_b += 1

    if (equipe_a >= 21) and ((equipe_a - equipe_b) > 1):
        print('Equipe A ganhou! com {}'.format(equipe_a))
        break

    
    if (equipe_b >= 21) and ((equipe_b - equipe_a) > 1):
        print('Equipe B ganhou! com {}'.format(equipe_b))
        break

    print('Placa: A: {} x B: {}'.format(equipe_a, equipe_b))
