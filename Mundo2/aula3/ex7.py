print ('Sequencia de fibonacci')
n1 = int (input('Qual o numeiro inteiro ? '))
n2 = int (input('Qual o tamanho da sequencia ? '))
c = 1
n3 = [0]
while c <= n2:
	c += 1
	print (f'{n1}-> ',end ='') 
	n3.append(n1)
	n3.sort()
	n1 += n3[-2]