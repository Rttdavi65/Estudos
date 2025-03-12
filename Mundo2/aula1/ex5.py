primeira_nota = float(input('Digite uma nota: '))
segunda_nota = float(input('Digite outra nota: '))
media = (primeira_nota + segunda_nota) / 2
print(f'Sua media foi: {media:.2f}')
if media < 5.0:
    print('Você foi reprovado! Estude mais!')
elif 5.0 <= media < 7.0:
    print('Infelizmente, Você está de recuperação, Estude mais para a prova final!')
elif media >= 7.0:
    print('Parabéns, você foi aprovado e passou de ano!')