nota1 = int(input('Digite a nota: '))
nota2 = int(input('Digite a nota: '))
nota3 = int(input('Digite a nota: '))
nota4 = int(input('Digite a nota: '))

if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:
    result = (nota2 + nota3 + nota4) / 3
elif nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    result = (nota1 + nota3 + nota4) / 3
elif nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    result = (nota2 + nota1 + nota4) / 3
else:
    result = (nota1 + nota2 + nota3) / 3

print(f'A média entre as notas é {result}')