from time import sleep
numb = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    sleep(2)
    print('{} x {:2} = {}'.format(numb, c, numb*c))