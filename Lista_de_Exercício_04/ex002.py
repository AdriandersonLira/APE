altura = float(input())
sexo = input()

if sexo == 'M':
    result = (72.7 * altura) - 58
else:
    result = (62.1 * altura) - 44.7

print(f'Peso ideal: {result}')
