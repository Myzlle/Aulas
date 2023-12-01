frase = str(input(' Qual é o seu nome completo?: '))
frase = frase.upper()
print(frase)
#Segundo Desafio Abaixo:
frase = str(input('Digite novamente o seu nome Completo! '))
frase = frase.lower()
print(frase)
#Terceiro DESAFIO abaixo:
frase = str(input('Digite o seu nome: ')).strip()
print('Seu nome ao todo {} letras'.format(len(frase) - frase.count(' ')))
#print('Seu primeiro tem {} letras:'.format(frase.find(' ')))
separa = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
