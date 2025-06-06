'''
Escreva um programa que solicite a altura e o peso de uma pessoa e calcule o indice de massa corporal (IMC), 
exibindo a categoria correspondente (abaixo do peso, peso normal, sobrepeso, obesidade, obesidade grave)
'''

altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))

imc = peso / altura ** 2

if imc <= 18.5:
	print('Abaixo do peso.')

elif imc >= 18.6 and imc <= 24.9:
	print('Peso normal.')
	
elif imc >= 25.0 and imc <= 29.9:
	print('Sobrepeso.')
	
elif imc >= 30.0 and imc <= 34.9:
	print('Obesidade.')
	
else:
	print('Obesidade grave.')
