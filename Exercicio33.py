'''
Escreva um programa que solicite um numero inteiro e verifique se e divisivel por 3 e por 5 ao mesmo tempo.
'''

n = int(input('Informe um numero: '))

if n % 3 == 0 and n % 5 == 0:
	print('Esse numero e divisivel por 3 e por 5.')
	
else:
	print('Esse numero nao e divisivel por 3 nem por 5.')