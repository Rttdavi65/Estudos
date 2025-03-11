cidade = input('Qual o nome da Cidade em que você mora? ')
dividir = cidade.split()
t = dividir[0].title()
setemsanto = 'Santo' in t
print(f'Sua cidade começa com Santo: {setemsanto}')