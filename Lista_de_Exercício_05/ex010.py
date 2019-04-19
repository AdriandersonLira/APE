# Declarações

from random import randint
jogo = 'Jogo do Arrocha!'

# Apresentação

print('~'*(len(jogo)+4))
print(' ', jogo)
print('~'*(len(jogo)+4))
print('\nSobre o jogo:\n')
string = 'Esse é um jogo que consiste em tentar adivinhar um número (previamente \
escolhido),\nque está representado dentro de um intervalo de números inteiros.\
 Inicialmente,\no jogador 1 prepara o jogo, definindo um intervalo e escolhendo um número (secreto)\n\
que está dentro desse intervalo, esse número escolhido não pode ser os números\nlimites do\
intervalo.\n\
Uma vez preparado o jogo, o jogador 2 tentará adivinhar esse número “chutando”\nvalores até\
acertar (ganha) ou arrochar o número (perde), ou informar valor \ninválido (perde). Um número é\
considerado inválido se estiver fora do intervalo\ndo jogo.\n'
print(string)

# Código geral

jogador1 = input('Nome jogador 1: ').title()
jogador2 = input('Nome jogador 2: ').title()

num_ini_jog_1 = int(input(f'{jogador1} digite o começo do intervalo: '))
num_fim_jog_1 = int(input(f'{jogador1} digite o final do intervalo: '))
number_secret = int(input('Digite o número secreto: '))

while True:
    print(num_ini_jog_1)
    print(num_fim_jog_1)
    chute = int(input(f'\n{jogador2} digite o "chute": '))
    if chute == number_secret: 
        print(f'\n{jogador2} ganhou!\n')
        break
    elif num_ini_jog_1 >= chute or chute >= num_fim_jog_1: 
        print(f'\n{jogador1} ganhou!\n')
        break
    elif num_ini_jog_1 < chute < num_fim_jog_1 and chute < number_secret: 
        num_ini_jog_1 = chute
        print('Tente novamente!\n')
    elif num_ini_jog_1 < chute< num_fim_jog_1 and chute > number_secret: 
        num_fim_jog_1 = chute
        print('Tente novamente!\n')