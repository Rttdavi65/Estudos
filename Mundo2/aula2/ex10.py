maior = 0
menor = 10000

for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c + 1}° pessoa: '))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O menor peso é {menor}Kg e o maior peso é {maior}Kg.')