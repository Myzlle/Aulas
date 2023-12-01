valor_casa = float(input("Valor da casa: "))
salario_comprador = float(input("Salário do comprador: "))
prazo_pagamento = int(input("Informe o número de parcelas que deseja paga: "))
parcela = valor_casa / prazo_pagamento

if  parcela <= 0.3 * salario_comprador:
    print("Empréstimo aprovado! Parabéns!")
else:
    print("Empréstimo negado. O valor excede 30% do salário.")