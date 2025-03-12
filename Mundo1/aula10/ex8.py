import math
a = float(input('Digite o primeiro lado: '))
b = float(input('o segundo: '))
c = float(input('o terceiro: '))
if a<= b+ c and b<= a + c and c<= a+b:
    if a > math.fabs(b-c) and b > math.fabs(c-a) and c > math.fabs(a-b):
        print('logo esses valores formam um triangulo')
    else:
        print('eles não formam um triangulo')
else:
    print('eles nao formam um triangulo')