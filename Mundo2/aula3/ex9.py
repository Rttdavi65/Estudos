resposta = "S"
soma = 0
quantidade = 0
maior = 0
menor = 0
primeira_vez = True

while resposta == "S":
    numero = int(input("Digite um número inteiro: "))
    soma = soma + numero
    quantidade = quantidade + 1

    if primeira_vez:
        maior = numero
        menor = numero
        primeira_vez = False
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    print("Deseja continuar? Digite S para sim ou N para não.")
    resposta = input().upper()

media = soma / quantidade

print("A média dos valores é:", media)
print("O maior valor foi:", maior)
print("O menor valor foi:", menor)
