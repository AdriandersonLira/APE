num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
ope = input('Informe o operando: ')
if ope != '+' and ope != '-' and ope != 'x' and ope != '/' and ope != '%':
    print('Operador desconhecido')
elif ope == '+':
    print('Resultado:', num1 + num2)
elif ope == '-':
    print('Resultado:', num1 - num2)
elif ope == 'x':
    print('Resultado:', num1 * num2)
elif ope == '/':
    print('Resultado:', num1 / num2)
else:
    print('Resultado:', num1 % num2)