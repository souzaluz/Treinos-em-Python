'''
Escreva um programa que solicite ao usuário um número N e diga se o mesmo é primo ou não.
'''
import math

N = int(input('Informe um número: '))

if N <2:
    print('O número não é primo')

else:
    eh_primo = True
    limite = math.ceil(math.sqrt(N))

    for i in range(2, limite+1):
        if N % i ==0:
            eh_primo = False
            break

    if eh_primo:
        print('O número é primo.')

    else:
        print('O número não é primo')