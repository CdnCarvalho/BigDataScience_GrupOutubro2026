
meta = 5000
vendedor = 1

continuar = 'S'

while continuar == 'S':

    vendas = float(input(f'Vendas do vendedor {vendedor}: R$ '))

    atingimento = (vendas / meta) * 100

    print(f'Vendas: R$ {vendas:.2f}')
    print(f'Atingimento: {atingimento:.2f}%')

    vendedor += 1

    continuar = input('\nDeseja cadastrar outro vendedor? (S/N): ').upper()

print('\nRegistro de vendas encerrado!')
# ---------------------------------------------------------------------------


META = 5000
vendedor = 1

continuar = 'S'

while continuar == 'S':

    vendas = float(input(f'Valor alcançado pelo vendedor {vendedor}: R$ '))

    atingimento = (vendas / META) * 100

    if atingimento >= 100:
        bonus = 500
    elif atingimento >= 70:
        bonus = 200
    else:
        bonus = 0

    print(f'\nVendedor {vendedor}')
    print(f'Atingimento da meta: {atingimento:.2f}%')
    print(f'Bônus: R$ {bonus:.2f}')

    vendedor += 1

    continuar = input('\nDeseja registrar outro vendedor? (S/N): ').upper()

print('\nApuração encerrada!')