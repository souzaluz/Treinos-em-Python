'''
Faça um programa que leia tres notas de um aluno e informe se ele foi aprovado(nota final maior ou igua a 7,0),
reprovado(nota final menor que 4,0) ou ficou de recuperaçao(nota final entre 4,0 e 7,0)
'''

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media_final = (nota1 + nota2 + nota3)/ 3

if media_final >= 7.0:
    print('Aprovado')

elif media_final > 4.0 and media_final < 7.0:
    print('Recuperação')

else:
    print('Reprovado')
