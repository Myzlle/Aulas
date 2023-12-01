v = int(input('Digite a velocidade que o veículo passou no radar: '))
m = (v-80) * 7
if v > 80:
    print('Você foi multado em: {}R$' .format(m))
else:
    print('Muito bem, continue dirigindo com responsabilidade, Tenha um Bom Dia!')
    