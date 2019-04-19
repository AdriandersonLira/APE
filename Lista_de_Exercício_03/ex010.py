nome = input()
tipo_ape = input()
num_diarias = int(input())
valor_de_consumo = float(input())

if tipo_ape == 'A': valor_diaria = 150
elif tipo_ape == 'B': valor_diaria = 100
elif tipo_ape == 'C': valor_diaria = 75
elif tipo_ape == 'D': valor_diaria = 50

valor_diarias = num_diarias * valor_diaria
subtotal = valor_diarias + valor_de_consumo
valor_taxa = (subtotal * 10) / 100
total = subtotal + valor_taxa
print(f'Nome do hóspede: {nome}\n\
        Tipo de Apartamento: {tipo_ape}\n\
        Número de diárias: {num_diarias}\n\
        Valor unitário da diária: {valor_diaria}\n\
        Valor total das diárias: {valor_diarias}\n\
        Valor consumo interno: {valor_de_consumo}\n\
        Subtotal: {subtotal}\n\
        Valor taxa de serviço: {valor_taxa}\n\
        Total: {total}')