soma = 0
contagem = 0
while True:
    valor = int(input('Digite qualquer número, 999 faz com que o programa termine. '))
    if valor == 999:
        break
    soma += valor
    contagem += 1

    

print(f'Foram digitados {contagem} números e a soma entre eles foi {soma}')
print('Programa terminando...')
exit()