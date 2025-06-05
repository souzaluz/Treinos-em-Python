p1 = input('Digite um valor: ')
p2 = input('Digite outro valor: ')

if p1 > p2:
    print(f'p1={p1} é maior que p2={p2}')
elif p2 > p1:
    print(f'p2={p2} é maior que p1={p1}')
else:
    print('Você digitou valores iguais.')