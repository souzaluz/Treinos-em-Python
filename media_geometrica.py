import math

numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe outro número: '))
numero3 = float(input('Informe mais um número: '))

media_geometrica = math.pow(numero1 * numero2 * numero3,  1/3)

print('A média geométrica dos números é: ', '{:.2f}'.format(media_geometrica))
