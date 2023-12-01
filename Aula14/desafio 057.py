sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: ')).upper()
    
    if sexo == 'M':
        print('Gênero Aceito: {}'.format(sexo))
    elif sexo == 'F':
        print('Gênero Aceito: {}'.format(sexo))
    else:
        print('Digite M ou F corretamente.')
