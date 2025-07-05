tupla = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))
qtd_nove = tupla.count(9)
print(f'Existem {qtd_nove} números noves')

for posicao, valor in enumerate(tupla):
    if valor == 3:
        print(f'O número 3 aparece na posição {posicao}')
        break
for n in tupla:
    if n % 2 == 0:
        print(f'{n} é par')