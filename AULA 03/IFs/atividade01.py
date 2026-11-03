# ATIVIDADE 01 - Desconto
# Sistema simples para aplicar desconto em compras acima de R$ 250,00

# Entrada do valor da compra
valor = float(input("Informe o valor da compra: R$ "))

# Verificação da condição para aplicar o desconto
if valor > 250:
    desconto = valor * 0.16  # Calcula 16% de desconto
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")



# ATIVIDADE 02 -
valor_vendas = float(input("Informe o valor das vendas: R$ "))

if valor_vendas >= 1000:
    total = valor_vendas + 150
    print(f"Excelente! Bônus de R$ 150,00. Total: R$ {total:.2f}")
elif valor_vendas >= 500:
    total = valor_vendas + 75
    print(f"Bom desempenho! Bônus de R$ 75,00. Total: R$ {total:.2f}")
else:
    print(f"Sem bônus. Valor das vendas: R$ {valor_vendas:.2f}")



# ATIVIDADE 03 -
valor = float(input("Digite o valor da compra: R$ "))

if valor < 100:
    desconto = 0
elif valor < 500:
    desconto = valor * 0.05
else:
    desconto = valor * 0.10

valor_final = valor - desconto

print("Valor da compra: R$", valor)
print("Desconto: R$", desconto)
print("Valor final: R$", valor_final)
