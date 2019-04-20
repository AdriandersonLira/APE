caractere = input()
if caractere.isalnum() == False:
    print(f'{caractere} é um caractere especial.')
elif caractere.isdigit == True:
    print(f'{caractere} é um número')
elif caractere.upper() == 'A' or caractere.upper() == 'E' or caractere.upper() == 'I' or caractere.upper() == 'O' or caractere.upper() == 'U':
    print(f'{caractere} é uma vogal')
else:
    print(f'{caractere} é uma consoante')