lista_nome = list()
while True:
    print('\
        MENU DE OPÇÕES: \n\
        1) Cadastrar nome \n\
        2) Pesquisar nome \n\
        3) Listar todos os nomes \n\
        0) Sair do programa\n\
    ')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        nome = input('Digite o nome a ser inserido: ').title()
        lista_nome.append(nome)
        print('\n  ---  Nome inserido com sucesso  ---\n')

    elif escolha == '2':
        nome_pesquisa = input('Digite o nome a ser pesquisado: ').title()
        if nome_pesquisa in lista_nome:
                print('\n  ---  Nome encontrado  ---\n')
                print(f'- {nome_pesquisa}\n')
                break
        else:  
            print('\n  ---  Nome não encontrado  ---\n')

    elif escolha == '3':
        print('\n  ---  Nomes cadastrados  ---\n')
        for n in lista_nome: print('- ',n)
        print('\n')

    elif escolha == '0': 
        break

    else: 
        print('\n  ---  Digite um número Válido  ---\n')