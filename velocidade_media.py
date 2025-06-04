deslocamento = float(input('Informe o espaço percorrido, em Km: '))
tempo = float(input('Informe o tempo gasto, em horas: '))

velocidade_media = deslocamento / tempo

print('A velocidade média é: ', '{:.2f}'.format(velocidade_media), 'Km/h')
