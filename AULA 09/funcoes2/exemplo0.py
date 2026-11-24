# Função criada para calcular o bônus da venda
def calcular_bonus(x):    
    b = x * 0.10 # Calcula 10% do valor da venda    
    t = x + b # Soma o valor da venda com o bônus

    # retorna dois valores bônus e total
    return b, t


n = float(input('Informe uma venda: '))

if n > 12000:
    bonus, total = calcular_bonus(n)
    print(f'\nValor da Venda R$ {n:.2f}')
    print(f'\nValor do Bônus R$ {bonus:.2f}')
    print(f'\nTotal com Bônus R$ {total:.2f}')

else:
    print(f'\nValor da Venda R$ {n:.2f}')
    print('Sem Bônus')
