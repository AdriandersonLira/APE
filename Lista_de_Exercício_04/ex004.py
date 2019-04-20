num = int(input('Digite um número(1 a 7): '))
semana = { 1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sábado' }
if semana[num] != 'Domingo' or semana[num] != 'Sábado':
    util = 'é dia útil'
else:
    util = 'não é dia útil'
print(f'{semana[num]} {util}')