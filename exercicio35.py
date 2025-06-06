'''
Faça um programa que solicite dois numeros e exiba se o primeiro e divisivel pelo segundo.
'''

n1 = int(input('Informe um numero: '))
n2 = int(input('Informe um numero: '))

if n1 % n2 == 0:
	print('O numero ', n1, ' e divisivel por', n2)
	
else:
	print('O numero ', n1, ' nao e divisivel por', n2)