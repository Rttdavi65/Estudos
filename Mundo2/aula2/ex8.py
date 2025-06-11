frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O Inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A Frase digitada não é um palídromo!')