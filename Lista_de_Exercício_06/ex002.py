while True:
    n = int(input())
    result = 'par' if n%2 == 0 else 'impar'
    print(f'Este número é {result}')
    saber = input('Deseja continuar? (Y/N): ')
    if saber == 'N':
        break
