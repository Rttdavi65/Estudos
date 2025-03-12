distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 201:
    preço = distancia * 0.50
    print(f'O Preço da passagem vai ser igual a {preço} reais.')
else:
    preço2 = distancia * 0.45
    print(f'O Preço da passagem vai ser igual a {preço2} reais.')