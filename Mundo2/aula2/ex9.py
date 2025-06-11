from datetime import date
maior = 0
menor = 0
atual = date.today().year

for c in range(0, 7):
    nasc = int(input(f'Informe o ano de nascimento da {c + 1}° pessoa: '))

    if atual - nasc >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Das sete pessoas, {maior} são maiores de idade e {menor} são menores de idade.')