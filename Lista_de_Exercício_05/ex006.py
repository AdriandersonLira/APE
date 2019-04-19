senha = '123'
cont = 0
while cont < 3:
    sen = input()
    if sen == senha:
        print('senha correta')
        break
    else:
        print('senha incorreta')
        cont += 1