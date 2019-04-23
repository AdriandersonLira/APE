ponto_A = 0
ponto_B = 0

while True:
    if ( ponto_A >= 21 and ponto_A - ponto_B >= 2 ) or ( ponto_B >= 21 and ponto_B - ponto_A >= 2 ):
        break
    saber = input('Qual equipe fez ponto ( A / B )? ').upper()
    if saber == 'A': ponto_A += 1
    elif saber == 'B': ponto_B += 1
    print(f'Equipe A {ponto_A} x {ponto_B} Equipe B')

if ponto_A > ponto_B: print('Equipe A ganhou o set')
else: print('Equipe B ganhou o set')