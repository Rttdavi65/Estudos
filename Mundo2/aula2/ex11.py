from time import sleep

media_idade = 0
maior_idade = 0
contado_m_menos20 = 0  
nome_mais_velho = ''

for c in range(1, 5):
    nome = input(f'Qual o nome da {c}° pessoa? ')
    sexo = int(input(f'[ 1 ] Masculino\n[ 2 ] Feminino\nQual seu sexo?:'))
    idade = int(input(f'Qual sua idade? '))

    media_idade = media_idade + idade

    if sexo == 1:
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome

    elif sexo == 2:
        if idade < 20:
            contado_m_menos20 = contado_m_menos20 + 1

media_idade = media_idade / 4

print('Analisando a lista...')
sleep(1)
print(f'''A média de idade do grupo é {media_idade}.
O homem mais velho é o {nome_mais_velho}, ele tem {maior_idade}.
Ao todo {contado_m_menos20} mulheres tem menos de 20 anos.''')