from random import choice
from time import sleep

jokenpo = ['Pedra','papel','Tesoura']
escolha_do_jogador = str(input('Qual Deseja escolher?\n[1] Pedra\n[2] Papel\n[3] Tesoura\n'))
escolha_do_pc = choice(jokenpo)
print('Estou escolhendo...')
sleep(3)
print('Escolhi! Vamos jogar!')
sleep(1)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(1)
#print(f'Eu joguei {escolha_do_pc}!')
if escolha_do_jogador == '1':
    if escolha_do_pc == [0]:
        print('Empate!')
elif escolha_do_jogador == '2':
    if escolha_do_pc == [1]:
        print('Empate!')
elif escolha_do_jogador == '3':
    if escolha_do_pc == [2]:
        print('Empate!')
