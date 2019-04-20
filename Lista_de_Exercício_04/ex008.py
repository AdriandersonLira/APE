total_vendas = int(input('Informe o total de vendas: '))
salario_minimo = 998
comissao = ( 5 * total_vendas ) / 100
if comissao < salario_minimo:
    salario = salario_minimo
else:
    salario = comissao
