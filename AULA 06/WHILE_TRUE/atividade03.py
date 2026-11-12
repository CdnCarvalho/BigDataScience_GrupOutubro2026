total_despesas = 0
quantidade = 0

while True:

    valor = float(input('Informe o valor da despesa: R$ '))

    total_despesas += valor
    quantidade += 1

    continuar = input('\nDeseja registrar outra despesa? (S/N): ').upper()

    if continuar == 'N':
        break

print('\nResumo das despesas')
print(f'Quantidade de registros: {quantidade}')
print(f'Total das despesas: R$ {total_despesas:.2f}')