# ------ COM DICIONARIO ------ #
'''
lista_estados = {
        'Acre': 0,  
        'Alagoas': 0,  
        'Amapá': 0,  
        'Amazonas': 0,  
        'Bahia': 0,  
        'Ceará': 0,  
        'Distrito Federal': 0,  
        'Espírito Santo': 0,  
        'Goiás': 0,
        'Maranhão': 0,  
        'Mato Grosso': 0,  
        'Mato Grosso do Sul': 0,  
        'Minas Gerais': 0,  
        'Pará ': 0,  
        'Paraíba': 0,  
        'Paraná': 0,  
        'Pernambuco': 0,  
        'Piauí': 0,  
        'Rio de Janeiro': 0,  
        'Rio Grande do Norte': 0,  
        'Rio Grande do Sul': 0,  
        'Rondônia': 0,  
        'Roraima': 0,  
        'Santa Catarina': 0,  
        'São Paulo': 0,  
        'Sergipe': 0,  
        'Tocantins': 0 
    }

while True:
    escolha = input('Digite um dos estados que você acha mais interessante: ').title()
    if escolha not in lista_estados:
        print('\n  ---  Esse estado não existe  ---\n')
        break
    else:
        lista_estados[escolha] += 1

cont = 0
estado = ''
for i in lista_estados:
    if lista_estados[i] > cont: 
        cont = lista_estados[i]
        estado = i
    elif lista_estados[i] == cont:
        estado += f', {i}'

if ',' in estado:
    print(f'Os estados mais votados foram: {estado}')
else:
    print(f'O estado mais votado foi: {estado}')

'''

# ------ COM LISTA ------ #

lista_estados = ['Acre','Alagoas','Amapá','Amazonas','Bahia','Ceará','Distrito Federal','Espírito Santo','Goias','Maranhão','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins']
lista_cont = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    escolha = input('Digite o nome do Estado: ')
    if escolha not in lista_estados:
        print('\n-- esse estado nao existe --\n')
        break
    else:
        for i in range(len(lista_estados)):
            if escolha == lista_estados[i]:
                lista_cont[i] += 1
    print(lista_cont)

cont = float('-Inf')
estado = ''
for i in range(len(lista_estados)):
    if lista_cont[i] > cont: 
        cont = lista_cont[i]
        estado = lista_estados[i]
    elif lista_cont[i] == cont:
        estado += f', {lista_estados[i]}'

if ',' in estado:
    print(f'Os estados mais votados foram: {estado} com {cont} votos')
else:
    print(f'O estado mais votado foi: {estado}  com {cont} votos')
