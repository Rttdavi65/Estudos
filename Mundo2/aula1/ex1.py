from time import sleep

print('-=-' *20)
print('Exercício 1')

valor_da_casa = float(input('Qual o valor desta casa? R$ ').strip())
salario_do_comprador = float(input('Qual o salário do comprador? R$ ').strip())
anos = int(input('Digite a quantidade de anos em que o comprador vai pagar ').strip())

prestacao = (salario_do_comprador*30)/100
valores = valor_da_casa/(anos*12)
if valores > prestacao:
    print('Seu emprestimo foi negado!')
    print(f'Valor de cada parcela: R${valores:.2f}\nLimite: R%{prestacao:.2f}')
    print('-=-' *20)
else:
    print(f'Parabéns, Seu emprestimo foi aprovado!\nO valor de cada parcela será: R${valores:.2f}')
    print('-=-' *20)
    sleep(2)
    exit()

