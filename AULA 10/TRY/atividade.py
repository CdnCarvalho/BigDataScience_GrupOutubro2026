print('''
========================
    Caixa Eletrônico
========================
''')


try:
    # saldo disponível na conta
    saldo = 1000

    saque = float(input('Informe o valor do saque: '))

# ocorre quando o usuário digita valores inválidos
except ValueError:
    print('Informe apenas números.')

except KeyboardInterrupt:
    print('Encerrado pelo usuário.')

else:
    # executa somente se NÃO ocorrer erro
    if saque > saldo:
        print('\nSaldo Insuficiente')

    # verifica se o saque é menor
    elif saque < 10:
        print('O valor precisa ser a partir de R$ 10')

    else:
        # realiza o saque
        saldo -= saque
        print('\nSaque realizado')
        print(f'Saldo restante de R$ {saldo}')

finally:
   # Sempre executa
    print('Operação Encerrada')
    exit()