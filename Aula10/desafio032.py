def eh_bissexto(ano):
    # Um ano é bissexto se for divisível por 4
    # No entanto, anos divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Solicita ao usuário para inserir um ano
ano_informado = int(input("Digite um ano para verificar se é bissexto: "))

# Chama a função e exibe o resultado
if eh_bissexto(ano_informado):
    print(f"{ano_informado} é um ano bissexto.")
else:
    print(f"{ano_informado} não é um ano bissexto.")

