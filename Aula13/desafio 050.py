soma = 0
cont = 0
for c in range (1, 7):
    numero = int(input('Digite o {} valor: '.format(c)))
    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1 
print(' Você informou {} números PARES, e a soma foi {}'.format(cont, soma))