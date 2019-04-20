nota1_prova1 = float(input('Digite uma das notas da prova 1: '))
nota2_prova1 = float(input('Digite próxima nota: '))
media_prova1 = (nota1_prova1 + nota2_prova1) / 2
if media_prova1 >= 7:
    nota1_prova2 = float(input())
    if nota1_prova2 >= 8:
        print('Esse candidato foi aprovado')
    else:
        print('Esse candidato foi reprovado')
else:
    print('Esse candidato não está apto para fazer a segunda prova.')