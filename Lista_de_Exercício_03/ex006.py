hora_ini = int(input('Horário de Início: '))
hora_fim = int(input('Horário de Fim: '))

if hora_ini < hora_fim:
    result = hora_fim - hora_ini
else:
    result = (hora_fim + 24) - hora_ini
print(f'Horário de termino do jogo: {result}')