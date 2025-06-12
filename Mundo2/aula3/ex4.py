from math import factorial
valor = int(input('Digite um valor qualquer'))
while not valor < 0:
    fatorial = factorial(valor)
    print(f'O Fatorial do valor dito é: {fatorial}')
    valor = int(input('Digite um valor qualquer'))
    