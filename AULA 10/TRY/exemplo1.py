# TRATANDO O ERROS DE VALORES INVÁLIDOS
print("\nMédia de produção Funcionário")
print("-"*30)

try:
    total_produzido = float(input("Informe o total das vendas: "))
    vendedores = int(input("Informe o total de vendederes: "))

    media = total_produzido / vendedores

    print(f'Média produzida: {media}')

except ValueError:
    print("\nErro - Informe apenas números")

# --------------------------------------------------------------------------------


# TRATANDO DIVISÃO POR ZERO E OS ERROS DE VALORES INVÁLIDOS
print("\nMédia por Funcionário")
print("-"*30)

try:
    total_produzido = float(input("Informe o total das vendas: "))
    vendedores = int(input("Informe o total de vendederes: "))
    
    media = total_produzido / vendedores

    print(f'Média produzida: {media}')

except ValueError:
    print("\nErro - Informe apenas números")

except ZeroDivisionError:
    print('Erro - Vendedor não pode ser zero - 0')

# ---------------------------------------------------------------------------------


# TRATANDO AS INTERRUPÇÕES DO TECLADO, DIVISÃO POR ZERO E VALORES INVÁLIDOS
for i in range(3):
    print("\nMédia por Funcionário")
    print("-"*30)
        
    try:
        total_produzido = float(input("Informe o total das vendas: "))
        vendedores = int(input("Informe o total de vendederes: "))
        
        media = total_produzido / vendedores

        print(f'Média produzida: {media:.2f}')

    except ValueError:
        print("\nErro - Informe apenas números")

    except ZeroDivisionError:
        print('Erro - Vendedor não pode ser zero - 0')
    
    except KeyboardInterrupt:
        print("\nPrograma encerrado")