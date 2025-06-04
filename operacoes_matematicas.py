numero1 = float(input("Informe um número: "))
numero2 = float(input("Informe outro número: "))

soma = numero1 + numero2
print(soma)

subtracao = numero1 - numero2
print(subtracao)

multiplicacao = numero1 * numero2
print(multiplicacao)

if numero2 != 0:
    divisao = numero1 / numero2
    print('A divisão dos números é: ', divisao)
else:
    print('Não é possível dividir por zero.')
