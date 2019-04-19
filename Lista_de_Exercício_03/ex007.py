peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
massa = peso / altura**2

if massa < 26:
    print('Normal')
elif 26 >= massa < 30:
    print('Obeso')
elif massa >= 30:
    print('Obeso Mórbido')
