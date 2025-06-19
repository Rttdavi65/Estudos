while True:
    print('-' * 20)
    valor = int(input('Qual valor deseja olhar a tabuada? '))
    print('-' * 20)
    if valor < 0:
        break
    for multiplicar in range(1,11):
        print(f'{valor} x {multiplicar} = {valor * multiplicar}')