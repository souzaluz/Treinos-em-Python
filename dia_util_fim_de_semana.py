'''
Faça um programa que solicite o nome de um dia da semana e exiba
se é um dia útil ou um dia de fim de semana.
'''

dia = input('Informe um dia da semana: ')

if dia.lower() == 'segunda' or dia.lower() == 'terça' or dia.lower() == 'quarta' or dia.lower() == 'quinta' or dia.lower() == 'sexta':
    print('É um dia útil')

elif dia.lower() == 'sábado' or dia.lower() == 'domingo':
    print('É um dia de fim de semana')

else:
    print('Dia inválido!')
