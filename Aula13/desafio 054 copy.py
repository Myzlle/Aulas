from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasci = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    idade = atual - nasci
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior')
    else:
        totmenor += 1
        print('Essa pessoa é de menor')

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
