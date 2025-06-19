soma = contador = 0
while True:
    valores = int(input('Digite um valor: '))
    if valores == 999:
        break
    soma += valores
    contador += 1
print(f'A Quantidade de números digitados foram: {contador} e a Soma entre eles é igual a {soma}.')