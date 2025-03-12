from calendar import isleap
ano = int(input('Em que ano você está? '))
if isleap(ano):
    print('é bissexto')
else:
    print('Não é bissexto')
