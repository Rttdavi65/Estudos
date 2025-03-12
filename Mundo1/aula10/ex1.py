from random import randint
escolha = str(randint(0,5))
advinhar = str(input('Qual numero você acha que o computador escolheu? entre 0 e 5?'))
if advinhar == escolha:
    print('Parabéns, você conseguiu advinhar!')
else:
    print('Infelizmente não foi dessa vez!')
print('Obrigado por jogar!')