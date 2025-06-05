nome = input('Informe seu nome: ')

qtde_letras = len(nome)

if (qtde_letras <= 4):
    print('Seu nome é curto')
elif (qtde_letras >= 5) and (qtde_letras <= 6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
