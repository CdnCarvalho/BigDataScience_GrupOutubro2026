for i in range(2):
    print("\nMédia por Funcionário")
    print("-"*30)
        
    try:
        total_produzido = float(input("Informe o total das vendas: "))
        vendedores = int(input("Informe o total de vendederes: "))
        
        media = total_produzido / vendedores


    except Exception as e:
        print(f"Erro Inesperado! {e}")
    
    else:
        print("\nDENTRO DO ELSE")
        print(f'Média produzida: {media:.2f}')

    finally:
        print("\nPrograma Encerrado")

#--------------------------------------------------------------------------------


