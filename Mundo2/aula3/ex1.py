sexo = str(input('Informe o seu Sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! Por favor, Informe o seu Sexo!')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')