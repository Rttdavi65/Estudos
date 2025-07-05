números = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
valor = int(input('Digite um valor entre 0 e 20: '))
while valor not in range(21):
    valor = int(input('Você digitou errado, Tente novamente: '))
    if valor in range(21):
        break
print(f'Você digitou o valor: {números[valor]}')
