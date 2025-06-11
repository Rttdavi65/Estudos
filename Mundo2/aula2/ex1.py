from time import sleep
from tqdm import tqdm
print('Os fogos de artificios serão lançados em:')
for c in range(10,-1, -1,):
    sleep(1)
    print(c)
sleep(1)
print('Os fogos foram lançados com Sucesso!')
for barra in tqdm([1,2,3,4,5]):
    sleep(0.5)
print('BOOM!!!')
sleep(3)
print('Estourou!')
