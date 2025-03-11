import random
n1 = str(input('Digite o Nome do primeiro aluno: '))
n2 = str(input('Digite o Nome do segundo aluno: '))
n3 = str(input('Digite o Nome do terceiro aluno: '))
n4 = str(input('Digite o Nome do quarto aluno: '))
l = (n1,n2,n3,n4)
e = random.choice(l)
print('Parabéns {}, você foi o escolhido!'.format(e))