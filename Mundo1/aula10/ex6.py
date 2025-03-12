n1 = float(input('Entre um valor:'))
n2 = float(input('Entre um valor:'))
n3 = float(input('Entre um valor:'))

if n1 > n2 > n3:
    print(f'O maior numero é {n1} e o menor numero é {n3}')
elif n2 > n3 > n1:
    print(f'O maior numero é {n2} e o menor numero e {n1}')
elif n3 > n2 > n1:
    print(f'O maior numero é {n3} e o menor numero e {n1}')
elif n1 > n3 > n2:
    print(f'O maior numero é {n1} e o menor numero e {n2}')
elif n2 > n1 > n3:
    print(f'O maior numero é {n2} e o menor numero e {n3}')
elif n3 > n1 > n2:
    print(f'O maior numero é {n3} e o menor numero e {n2}')