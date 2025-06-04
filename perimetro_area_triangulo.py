a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))
h = float(input('Informe o valor de h: '))

perimetro = a + b + c
area = (b * h)/2

print('O perímetro do triângulo é: ', '{:.2f}'.format(perimetro))
print('A área do triângulo é: ', '{:.2f}'.format(area))
