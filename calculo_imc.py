peso = float(input('Informe o seu peso (em kg): '))
altura = float(input('Informe sua altura (em m): '))
imc = peso / altura ** 2
print('O seu Índice de Massa Corporal é: ', '{:.2f}'.format(imc))
