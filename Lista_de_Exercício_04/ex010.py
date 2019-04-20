ano = int(input('Digite o ano: '))
result = 'é bissexto' if ano%4 == 0 and ano%400 == 0 and ano%100 != 0 else 'não é bissexto'
print(f'{ano} {result}')