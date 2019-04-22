menor = float('inf')
maior = float('-inf')
for i in range(30):
    temperatura = float(input('Digite a temperatura: '))
    if temperatura > maior: maior = temperatura
    elif temperatura < menor: menor = temperatura

print(f'A maior temperatura desse mês foi: {maior}')
print(f'A menor temperatura desse mês foi: {menor}')