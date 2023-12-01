'''nome = str(input('Digite o nome da sua cidade: '))
print('A cidade informada {}, não é Santo'.format(nome.find('Santo')))'''

cidade = str(input(' Qual cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')