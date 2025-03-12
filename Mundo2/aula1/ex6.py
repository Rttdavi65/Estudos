from datetime import date
ano_de_nascimento = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - ano_de_nascimento
print(f'O(a) atleta tem {idade} anos')
if idade <= 9:
    print('Ele(a) é classificado(a) como: Mirim!')
elif idade <= 14:
    print('Ele(a) é classificado(a) como: Infantil!')
elif idade <= 19:
    print('Ele(a) é classificado(a) como: Junior!')
elif idade == 20:
    print('Ele(a) é classificado(a) como: Sênior!')
elif idade > 20:
    print('Ele(a) é classificado(a) como: MASTER!')