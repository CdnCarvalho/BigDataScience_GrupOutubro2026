valores = []

for i in range(10):
    numero = float(input('Informe o valor da venda: '))
    valores.append(numero)

print(f'Total das vendas: R$ {sum(valores):.2f}')