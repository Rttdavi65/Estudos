palavras = ('Arroz','Pato','Objeto','Sapato')
for p in palavras:
    print(f'Na palavra {p} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)