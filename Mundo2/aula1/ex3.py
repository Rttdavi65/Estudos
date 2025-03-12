primeiro_valor = int(input('Digite um numero inteiro: '))
segundo_valor = int(input('Digite um outro numero inteiro: '))
if primeiro_valor > segundo_valor:
    print(f'O Primeiro Numero {primeiro_valor} é maior que o Segundo Numero {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'O Segundo Numero {segundo_valor} é maior que o Primeiro Numero {primeiro_valor}')
elif primeiro_valor == segundo_valor or segundo_valor == primeiro_valor:
    print('Os dois numeros são iguais!')