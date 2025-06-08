'''
Escreva um programa que solicite ao usuário um número N e exina todos os 
números primos menores que N.
'''

import math

N = int(input('Informe um número: '))

def eh_primo(N):
    if N < 2:
        return False
    
    limite = math.isqrt(N) + 1

    for i in range(2, limite):
        if N % i == 0:
            return False
        
    return True

num = int(input('Informe um número inteiro: '))

print('Números primos menores que ', num, ': ')

for numero in range(2, num):
    if eh_primo(numero):
        print(numero)