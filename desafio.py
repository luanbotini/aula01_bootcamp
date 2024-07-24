# Cálculo de bônus com entrada do usuário (Bônus = 1000 + salario * bônus )

nome = input("Qual é o seu nome? ")
salario = float(input("Qual é o seu salário? "))
bonus = float(input("Qual é o valor do bônus que recebeu? "))
valor_bonus = 1000 + salario*bonus
print(f"O usuário {nome} possui o bonus de {valor_bonus}")