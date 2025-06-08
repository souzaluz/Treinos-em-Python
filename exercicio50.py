'''
Escreva um programa que leia números do usuário
até que seja digitado um número negativo, e exiba
a soma dos números positivos.
'''
soma = 0

while True:
    numero = int(input('Informe um número (negativo para encerrar): '))

    if numero < 0:
        break

    if numero >= 0:
        soma += numero
print('A soma dos números positivos é: ', soma)