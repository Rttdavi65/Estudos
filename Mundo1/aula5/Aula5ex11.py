d = float(input('Quantos Dias alugados? '))
k = float(input('Quantos Km rodados? '))
pago = (d * 60) + (k * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
