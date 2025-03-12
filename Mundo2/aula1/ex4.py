idade = int(input('Quantos anos você tem? '))
if idade-18 == 0:
    print('Está na hora de se alistar ao serviço militar!')
elif idade > 18:
    print(f'Já passou da hora de se alistar ao serviço militar! Você devia ter se alistado há {idade-18} anos!')
elif idade < 18:
    print(f'Ainda vai ter que se alistar, mas não chegou a hora ainda! Daqui a {18-idade} você vai poder se alistar.')