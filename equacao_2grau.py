import math

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de a: '))

delta = b ** 2 - 4 * a * c
print('O valor de delta é:', delta)

if (delta > 0):
    x1 = float(-b + math.sqrt(delta))
    x2 = float(-b - math.sqrt(delta))
    print('As raízes da equação de segundo grau são, x1: ', '{:.2f}'.format(x1), 'e x2: ', '{:.2f}'.format(x2))

else:
    print('O valor de delta é negativo')
