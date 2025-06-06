'''
Crie um progama que solicite a idade de uma pessoa e exiba se ela e criança (0 - 12 anos),
adolescente (13 - 17 anos), adulta (18 - 59 anos) ou idosa (60 ou mais anos).
'''

idade = int(input("Informe a idade: "))

if idade <= 12:
	print('Essa pessoa e uma criança.')
	
elif idade >= 13 and idade <= 17:
	print('Essa pessoa e uma adolescente.')
	
elif idade >= 18 and idade <=59:
	print('Essa pessoa e uma adulta.')
	
else:
	print('Essa pessoa e uma idosa.')
