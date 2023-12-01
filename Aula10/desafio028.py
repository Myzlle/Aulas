import random
nome = int(input('Qual o número estou pensando? entre 0 e 5: '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

if escolhido == nome:
    print('True')
else:
    print('False')

print('--FIM--')
print('O escolhido foi {}'.format(escolhido))


