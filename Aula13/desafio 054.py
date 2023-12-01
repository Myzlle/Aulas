from datetime import date
atual = date.today().year
for pessoa in range (1, 8):
    nasci = int(input('Em que ano a pessoa nasceu?  '))
    idade = atual - nasci
    if idade >= 21:
        print('Essa pessao é maior')
    else:
        print('Essa pessoa é de menor')