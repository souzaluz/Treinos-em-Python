while True:
    numero1 = input('Informe um número: ')
    numero2 = input('Informe outro número: ')
    operador = input('Informe o operador (+-/*): ')

    numeros_validos = None
    num1_int = 0
    num2_int = 0

    try:
        num1_int = int(numero1)
        num2_int = int(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido. ')
        continue
    
    if len(operador) >1:
        print('Digite apenas um operador. ')
        continue

    print('Realizando sua conta. Confira o resultado abaixo: ')

    if operador == '+':
        print(f'{num1_int} + {num2_int}=', num1_int + num2_int)
    elif operador == '-':
        print(f'{num1_int} - {num2_int}=', num1_int - num2_int)
    elif operador == '/':
        print(f'{num1_int} / {num2_int}=', num1_int / num2_int)
    elif operador == '*':
        print(f'{num1_int} * {num2_int}=', num1_int * num2_int)
    else:
        print('Nunca deveria chegar aqui.')   

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break