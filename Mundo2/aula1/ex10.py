from random import choice
from time import sleep

print('-=-' *10)
titulo = 'JOKENPÔ!'
print(f'{titulo :^26}')

def jokenpo():
    escolha = ['pedra', 'papel', 'tesoura']
    jogador = str(input('Escolha uma opção:\nPedra\nPapel\nTesoura\n '.strip().title()))
    
    if jogador not in escolha:
        print('Opção invalida!')
        return
    
    pc = choice(escolha)
    print(f'A Escolha da maquina foi: {pc}')

    if jogador == pc:
        print('Empate!')
    elif (jogador == 'pedra' and pc == 'tesoura') or \
         (jogador == 'papel' and pc == 'pedra') or \
         (jogador == 'tesoura' and pc == 'papel'):
        print('Você venceu!')
    else:
        print('Você perdeu!')
jokenpo()