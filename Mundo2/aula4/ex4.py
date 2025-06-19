maior_de_idade = homens = mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('O Sexo é [M/F]? ')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if idade > 17:
        maior_de_idade += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'O Número de pessoas cadastradas +18 anos foram: {maior_de_idade} \nA Quantidade de homens cadastrada foram: {homens}\nA Quantidade de mulheres -20 anos foram: {mulheres}')