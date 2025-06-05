numero = input('Informe um número: ')

if numero.isdigit():
    numero_int = int(numero)

    if (numero_int % 2 == 0):
        print('Este número é par.')
    else:
        print('O número é ímpar.')

else:
    print('Você não digitou um número inteiro.')