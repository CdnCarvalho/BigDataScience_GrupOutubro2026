valor = float(input('Informe o valor: '))

print('''
FORMAS DE PAGAMENTO:
[1] - PIX (12% de desconto)
[2] - DÉBITO (8% de desconto)
[3] - CRÉDITO (5% de desconto)
[4] - DINHEIRO (15% de desconto)
''')

desconto = 0
opcao = int(input('\nInforme a opção: '))
# operacao = True

match opcao:
    case 1:
        print('------ Pagamento em PIX ------')
        desconto = valor * 0.12
    case 2: 
        print('------ Pagamento em DÉBITO ------')
        desconto = valor * 0.08
    case 3:
        print('------ Pagamento em CRÉDITO ------')
        desconto = valor * 0.05
    case 4:
        print('------ Pagamento em DINHEIRO ------')
        desconto = valor * 0.15
    case _:
        operacao = False
        print('Opção inválida!')

# if desconto != 0:
# if operacao == True:  # P/ isso precisa criar a variável operacao
if opcao in [1, 2, 3, 4]:
    valor_final = valor - desconto
    print(f'Preço normal: R$ {valor:.2f}')
    print(f'Valor do desconto: R$ {desconto:.2f}')
    print(f'Total à Pagar: R$ {valor_final:.2f}')
else: 
    print('Escolha uma opção acima.')