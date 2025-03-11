from unidecode import unidecode

f = input('Escreva uma frase: ').lower()
frase = unidecode(f)
print('A letra "A" aparece {} vezes.' .format(frase.count('a')))
print('A primeira vez que "A" aparece é {}' .format(frase.find('a')))
print('A última vez que "A" aparece é {}' .format(frase.rfind('a')))