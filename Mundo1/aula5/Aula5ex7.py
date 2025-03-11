pr = float(input('Qual é o preço do produto? R$'))
des1 = pr*5/100
des2 = pr-des1
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(pr,des2))