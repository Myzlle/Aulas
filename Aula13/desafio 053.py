frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inversor = ''

for letra in range(len(junto)-1, -1, -1):
    inversor += junto[letra]

print('O inversor de {} é {}'.format(junto, inversor))

if inversor == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')