n = int(input('Informe um número: '))
e = int (input('Informe um expoente: '))

potencia = 1

if e>0:
    contador = 0
    while contador < e:
        potencia *= n
        contador += 1

elif e<0:
    contador = 0
    while contador > e:
        potencia /= n
        contador-= 1

print(potencia)