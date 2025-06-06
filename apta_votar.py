'''
Faça um programa que leia a idade de uma pessoa e informe se ela não está a votar,
se á apta a votar, mas nao é obrigada (16, 17 anos ou idade igual ou superior a 70 anos)
ou se é obrigada (18 a 69 anos) 
'''

idade = int(input('Informe a idade: '))

if idade < 16:
    print('Não está apta a votar.')

elif idade >= 18 and idade <= 69:
    print('Está apta e é obrigda a votar.')

else:
    print('Está apta a votar, mas não é obrigada.')
