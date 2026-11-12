total_arrecadado = 0

for venda in range(5):
    valor = float(input(f'Valor da venda {venda}: R$ '))

    if valor >= 200:
        desconto = valor * 0.10
    else:
        desconto = 0

    valor_final = valor - desconto
    total_arrecadado += valor_final

    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Valor final: R$ {valor_final:.2f}')

print(f'\nTotal de descontos concedidos: R$ {total_arrecadado:.2f}')