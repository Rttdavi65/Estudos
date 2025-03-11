numero = input('Digite um número de 0 a 9999: ')
resultado = '000'+ numero
print(f'Unidade {(resultado[-1])}') 
print(f'Dezena {(resultado[-2])}') 
print(f'Centena {(resultado[-3])}') 
print(f'Milhar {(resultado[-4])}') 
