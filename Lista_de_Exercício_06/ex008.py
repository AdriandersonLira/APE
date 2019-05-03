massa = float(input('Digite a quantidade de massa: '))
tempo = 0
while massa >= 0.5:
    tempo += 50
    massa /= 2
print(f'{tempo} segundos para a massa se tornar menor que 0,5g')
