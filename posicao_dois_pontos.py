import math

x1 = float(input('Informe a posição x1: '))
x2 = float(input('Informe a posição x2: '))
y1 = float(input('Informe a posição y1: '))
y2 = float(input('Informe a posição y2: '))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('A distância entre os pontos é: ', '{:.2f}'.format(d))
