# Função responsável por calcular o desconto da compra
def calcular_desconto(valor):

    # Calculando 16% de desconto sobre o valor informado
    desconto = valor * 0.16

    # Subtraindo o desconto do valor original da compra
    total = valor - desconto

    # Retornando o valor final com desconto
    return total



# Solicita ao usuário o valor da compra
valor = float(input('Informe o valor da compra: R$ '))


# Verifica se o cliente possui direito ao desconto
if valor > 250:

    # se o valor for acima de 250, entra no if
    # Chamando a função para calcular o desconto,
    # e recebe o retorno da função na variável total_desconto
    total_desconto = calcular_desconto(valor)

    # Exibindo a mensagem de desconto aplicado
    print(f'Você ganhou 16% de DESCONTO.')

    # Exibindo o valor final da compra com desconto
    print(f'Valor total com desconto: R$ {total_desconto:.2f}')

else:

    # Caso a compra não atinja o valor mínimo para desconto
    print(f'O valor total da compra é de: R$ {valor:.2f}')


# Mensagem final do sistema
print('Obrigado por comprar conosco. Volte sempre!')