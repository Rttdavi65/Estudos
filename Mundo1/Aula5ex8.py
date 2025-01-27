au = float(input('Qual é o salário do Funcionário? R$'))
s1 = au*15/100
s2 = au+s1 
print('Um Funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(au,s2))