vendas = []

# Cadastro das 5 vendas
for i in range(5):
    valor = float(input(f"Digite o valor da venda {i + 1}: "))
    vendas.append(valor)

# Cálculos
total = sum(vendas)
media = total / len(vendas)

# Resultados
print("\n--- Relatório de Vendas ---")
print(f"Vendas realizadas: {vendas}")
print(f"Total vendido: R$ {total:.2f}")
print(f"Média das vendas: R$ {media:.2f}")