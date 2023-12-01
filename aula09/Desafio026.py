'''frase = str(input('Digite o seu nome completo ')).strip().upper()
print('A letra ''A'' apareceu: {} vezes no nome.'.format(frase.count('A')))
print('A primeira letra ''A'' aparceu na posição: {}'.format(frase.find('A')+1))
#print('A letra A apareceu na útilma posição: {}'.format(frase.rfind('A')+1))'''  

frase = str(input('Informe o seu nome completo: ')).strip().upper()
f1 = frase.count('A')
f2 = frase.find ('A')+1
f3 = frase.rfind('A')+1
print('A letra a, apareceu: {} vezes no nome.'.format(f1))
print('A PRIMEIRA: letra a, apareceu na posição: {}'.format(f2))
print('A letra a, apareceu quantas vezes na última posição?: {}'.format(f3))


