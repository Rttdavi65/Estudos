numero = int(input('Digite um numero inteiro: '.strip()))
conversao = str(input('Para qual deseja converter?\n[1] binário\n[2] octal\n[3] hexadecimal\n'))
if conversao == '1':
    print(f'Convertido para binário é igual a {bin(numero)[2:]}')
elif conversao == '2':
    print(f'Convertido para octal é igual a {oct(numero)[2:]}')
elif conversao == '3':
    print(f'Convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Digite uma opção valida!')