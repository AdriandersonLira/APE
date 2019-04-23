sbt = 0 ; globo = 0 ; band = 0 ; record = 0
numero_total = 0
while True:
    canal = int(input('Digite o canal: '))
    numero_de_pessoas = int(input('Número de pessoas: '))
    numero_total += numero_de_pessoas 
    if canal == 0: break
    elif canal == 5: sbt += numero_de_pessoas 
    elif canal == 7: globo += numero_de_pessoas
    elif canal == 10: band += numero_de_pessoas
    elif canal == 12: record += numero_de_pessoas

quant = sbt + globo + band + record
percentualcanal5  = (sbt*100)    / quant
percentualcanal7  = (globo*100)  / quant
percentualcanal10 = (band*100)   / quant
percentualcanal12 = (record*100) / quant

print(f'O Percentual de audiencia do canal 5 é: {percentualcanal5}')
print(f'O Percentual de audiencia do canal 7 é: {percentualcanal7}')
print(f'O Percentual de audiencia do canal 10 é: {percentualcanal10}')
print(f'O Percentual de audiencia do canal 12 é: {percentualcanal12}')
