n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opção = str(input('>>>>>Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A Soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O Resultado do {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Digite os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')