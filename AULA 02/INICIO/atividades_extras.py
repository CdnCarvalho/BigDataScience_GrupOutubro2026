
# ATIVIDADE 1
# 1. Crie um programa que leia um número e mostre o seu anterior e o seu sucessor.
# E mostre-os no final.
num = int(input("Digite um número: "))
anterior = num - 1
sucessor = num + 1
print(f"O número anterior é {anterior}")
print(f"E o sucessor é {sucessor}")
# --------------------------------------------------------------------------------------



# ATIVIDADE 2
# 1. Crie um programa que leia um número e mostre seu dobro, triplo e o quadrado.
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
quadrado = num ** 2
print(f"O dobro de {num} é {dobro}")
print(f"O triplo de {num} é {triplo}")
print(f"O quadrado de {num} é {quadrado}")
# --------------------------------------------------------------------------------------



# ATIVIDADE 3
# Enunciado: Descubra quantos ingressos de cinema podem ser comprados com o valor disponível.
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
valor_disponivel = float(input("Digite quanto dinheiro você tem para a compra: "))
quantidade = float(valor_disponivel // preco_unitario)
troco = float(valor_disponivel % preco_unitario)
print(f"Com R$ {valor_disponivel}, você pode comprar {quantidade}, ingresso(s). O troco é R$ {troco:.2f}")
# ------------------------------------------------------------



# ATIVIDADE 4 - Aumento de salário
# Enunciado: Calcule o novo salário de um funcionário com aumento de 15%.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)
