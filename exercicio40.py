'''
Crie um programa que solicite ao usuario um numero e exiba a tabuada desse numero utilizando um laço de repetiçao.
'''
n = int(input('Informe um numero: '))

contador = 0

for i in range(11):
	tabuada = n * contador
	print(n,  ' * ', contador, '=', tabuada)
	contador += 1