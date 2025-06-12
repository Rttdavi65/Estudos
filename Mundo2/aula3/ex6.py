a1 = int(input('Qual o primeiro termo de uma P.A.? '))
r = int(input('E qual é a razão dessa mesma P.A.? '))
ct = 0
print(f'\nOS 10 PRIMEIROS TERMOS DESSA P.A. SÃO:\n{a1}')
while ct <9:
    ct = ct + 1
    print(a1 + r*ct)
v = -1
while v != 0:
    v = int(input('Você deseja ver mais quantos termos? '))
    a2 = a1 + r*9
    ct = 0
    while ct < v:
        ct = ct + 1
        print(a2 + r*ct)
print('Programa encerrado!')