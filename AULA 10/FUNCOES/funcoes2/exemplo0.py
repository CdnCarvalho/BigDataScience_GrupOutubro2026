# Função criada para calcular o bônus da venda
def calcular_bonus(x):    
    b = x * 0.10 # Calcula 10% do valor da venda     
    t = x + b # Soma o valor da venda com o bônus
    
    return b, t  # o bônus calculado e o total com bônus


# Usuário digita o valor da venda
n = float(input('Informe uma venda: '))

# Verifica se a venda é maior que 12000
if n > 12000:

    # Chamando a função calcular_bonus()
    # O primeiro valor retornado vai para a variável bonus
    # O segundo valor retornado vai para a variável total
    bonus, total = calcular_bonus(n)

    # Mostrando o valor original da venda
    print(f'\nValor da Venda R$ {n:.2f}')
    # Mostrando o valor do bônus
    print(f'\nValor do Bônus R$ {bonus:.2f}')
    # Mostrando o valor total com o bônus acrescentado
    print(f'\nTotal com Bônus R$ {total:.2f}')

else:

    # Caso a venda não atinja o valor mínimo para bônus
    print(f'\nValor da Venda R$ {n:.2f}')
    print('Sem Bônus')
