valor = float(input('Digite o valor do produto: R$'))
print('''Escolha um método de pagamento abaixo:

[ 1 ] A vista no dinheiro ou nocheque com 10% de desconto.
[ 2 ] A vista no cartão com 5% de desconto. 
[ 3 ] Parcelado 2x no cartão (sem desconto)
[ 4 ] Parcelado 3x ou mais no cartão com 20% de juros''')

p = int(input('Sua escolha: '))



if p == 1:
    total = valor-(valor*10/100)
elif p == 2:
    total = valor-(valor*5/100)
elif p == 3:
    total = valor
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif p == 4:
    total = valor+(valor*20/100)
    tpd = int(input('Digite quantas vezes deseja parcelar: '))

    parcela = total/tpd
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% de juros'.format(tpd, parcela))
else:
    total = 0
    print('Ocorreu um erro, verifique o que você digitou e tente novamente!')

print('produto de R${:.2f} vai custar R${:.2f} no total!'.format(valor, total))