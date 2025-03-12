velocidade = float(input('Em que velocidade você esteve? '))
multa = 0
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print(f'Sua multa foi de {multa} reais')
else:
    print('Você não foi multado!')