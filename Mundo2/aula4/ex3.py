from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-' * 20)
contagem = 0
while True:
    computador = randint(1,10)
    par_impar = str(input('Deseja escolher PAR ou IMPAR? [P/I]')).strip().upper()
    while not par_impar == 'P' and not par_impar == 'I':
        print('Você digitou errado! Tente novamente!')
        par_impar = str(input('Deseja escolher PAR ou IMPAR? [P/I]')).strip().upper()
        if par_impar == 'P' and 'I':
            break
    while True:
        valor = int(input('Digite um valor de 1 a 10: '))
        while valor > 10:
            print(f'Você não tem {valor} dedos!')
            valor = int(input('Digite um valor de 1 a 10: '))
        break
    soma = valor + computador
    print(f'O Computador escolheu {computador} e Você {valor}, a soma deu: {soma}')
    if soma % 2 == 0 and par_impar == 'P' or soma % 2 != 0 and par_impar == 'I':
        contagem += 1
        print('Você ganhou!')
    else:
        break
print(f'Você perdeu após {contagem} vitorias!')