'''
Escreva um programa que exiba todos os numeros pares de 1 a 100.
'''
for i in range (0, 102, 2):
	print(i)

contador = 0

while contador <= 100:
	if contador % 2 ==0 and contador <= 50:
		print(contador)
		
	else:
		print(contador)
		
	contador += 1