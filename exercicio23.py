n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
n3 = int(input('Informe mais um número: '))

soma = n1 + n2 + n3

if (soma % 5 == 0):
    print('A soma é divisível por 5.')

else:
    print('A soma não é divisível por 5.')