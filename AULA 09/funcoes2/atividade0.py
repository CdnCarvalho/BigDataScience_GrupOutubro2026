# Função responsável por calcular o desconto da compra
def calcular_desconto(valor):    
    desconto = valor * 0.16 # Valor de 16% de desconto    
    total = valor - desconto   # Subtraindo o desconto

    # Retornando o resultado
    return total


# Solicita o valor da compra
valor = float(input('Informe o valor da compra: R$ '))

# Verifica se o cliente possui direito ao desconto
if valor > 250:
    total_desconto = calcular_desconto(valor)
    print(f'Você ganhou 16% de DESCONTO.')
    print(f'Valor total com desconto: R$ {total_desconto:.2f}')

else:
    print(f'O valor total da compra é de: R$ {valor:.2f}')
    
print('Obrigado por comprar conosco. Volte sempre!')