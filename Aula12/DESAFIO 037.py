# Obter número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Obter escolha da base de conversão do usuário
opcao = int(input("Escolha a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\n"))

# Realizar a conversão com base na escolha
if opcao == 1:
    resultado = bin(numero)[2:]  # Remover o prefixo '0b' da representação binária
elif opcao == 2:
    resultado = oct(numero)[2:]  # Remover o prefixo '0o' da representação octal
elif opcao == 3:
    resultado = hex(numero)[2:]  # Remover o prefixo '0x' da representação hexadecimal
else:
    resultado = "Opção inválida"

# Exibir o resultado
print(f'O resultado da conversão é: {resultado}')
