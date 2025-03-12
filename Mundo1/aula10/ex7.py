from time import sleep
salario = float(input('Digite quanto você recebe: '))
print('So um momento...')
sleep(2)
if salario > 1250:
    novo_salario = salario * 1.10
    print(f'Seu salario é de {novo_salario} reais.')
else:
    if salario <= 1251:
        novo_salario2 = salario * 1.15
        print(f'Seu salario é de {novo_salario2} reais.')
