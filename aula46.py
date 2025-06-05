""" 
No Python as strings são iteráveis, ou seja, pode-se pegar letra por letra
(via índice, que pode ser positivio ou negativo)
Fatiamento [i:f:p][::]
Pode-se pegar uma parte da string no início, no fim ou uma parte qualquer.
No fatiamento de strings, dentro de colchetes, coloca-se o índice de onde 
vai começar o fatiamento e se quiser printar até o final da string, não precisa
colocar o índice final. Mas separa-se os índices por dois pontos (:)

no Python, tem a função len que retorna a quantidade de caracteres da string.
"""
variavel = 'Olá mundo!'
#print(variavel[-4:8])
#print(len(variavel))
print(variavel[0:9:2])
