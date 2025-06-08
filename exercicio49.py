'''
Escreva um programa que solicite ao usuário dois números
A e b e exiba todos os números entre A e B.
'''
A = int(input('Informe um número: '))
B = int(input('Informe outro número: '))

print('Os números entre ', A, ' e ', B ,' são: ')

if A <= B:
  for num in range(A, B + 1):
    print(num)

else:
  for num in range(A, B - 1, -1):
    print(num)