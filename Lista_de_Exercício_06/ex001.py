while True:
    print('OPÇÕES:')
    print('1 - SAUDAÇÃO')
    print('2 - BRONCA')
    print('3 - FELICITAÇÃO')
    print('0 - FIM')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('\nOlá. Como vai?\n')
    elif opcao == 2:
        print('\nVamos estudar mais.\n')
    elif opcao == 3:
        print('\nMeus Parabéns!\n')
    else:
        print('Fim de serviço.')
        break