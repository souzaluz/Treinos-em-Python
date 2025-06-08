'''
Escreva um programa que solicite ao usuario um numero N e exiba a soma de todos os numeros de 1 a N.
'''
N = int(input('Informe um numero: '))

contador = 0
soma = 0

while contador <= N:
	soma += contador
	#soma_final = soma + contador	
	contador += 1
	
print(soma)