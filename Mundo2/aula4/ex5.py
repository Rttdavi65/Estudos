contagem = total = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    contagem += 1
    total += preço
    continuar = str(input('Quer continuar? [S/N] ')).upper().capitalize()
    if continuar == 'N':
        break
    if preço > 1000:
        contagem += 1 
    if contagem == 1 or preço < menor:
        menor = preço
        barato = produto
print(f'O Total da compra foi R${total}\nTemos {contagem} produtos custando mais de R$1000.00\nO Produto mais barato foi {barato} que custa R${menor}')