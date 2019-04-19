cont_mulheres = 0
cont_homens = 0
cont_solteiros = 0
cont_casados = 0
media_salario_mulheres = 0
media_idade_homens = 0
cont_mulheres_solteiras_acima_2000 = 0
cont_homens_mais_35_acima_2000 = 0

for i in range(5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')
    estado_civil = input('Estado Civil: ')
    salario = float(input('Salario: '))
    if sexo == 'feminino': cont_mulheres += 1; media_salario_mulheres += salario
    elif sexo == 'masculino': cont_homens += 1; media_idade_homens += idade
    if estado_civil == 'solteiro': cont_solteiros += 1
    elif estado_civil == 'casado': cont_casados += 1
    if sexo == 'feminino' and estado_civil == 'solteira' and salario > 2.000:
        cont_mulheres_solteiras_acima_2000 += 1
    if sexo == 'masculino' and idade > 35 and salario > 2.000:
        cont_homens_mais_35_acima_2000 += 1

print('a) A quantidade de mulheres entrevistadas: ', cont_mulheres)
print('b) A quantidade de homens entrevistados: ', cont_homens)
print('c) A quantidade de pessoas solteiras: ', cont_solteiros)
print('d) A quantidade de pessoas casadas: ', cont_casados)
print('e) O salário médio das mulheres entrevistadas: ', media_salario_mulheres/cont_mulheres)
print('f) A idade média dos homens entrevistados: ', media_idade_homens/cont_homens)
print('g) A quantidade de mulheres solteiras que ganham acima de R$ 2.000,00: ', cont_mulheres_solteiras_acima_2000)
print('h) A quantidade de homens com mais de 35 anos que ganham acima de R$ 2.000,00: ', cont_homens_mais_35_acima_2000)
