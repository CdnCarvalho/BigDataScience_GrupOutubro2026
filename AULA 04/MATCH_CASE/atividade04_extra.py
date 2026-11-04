# COD-13
valor = float(input("Valor do ingresso: R$ "))

opcao = int(input("""
TIPO DE INGRESSO
1 - Inteira
2 - Meia (50% desconto)
3 - Promoção (30% desconto)
Escolha: """))

desconto = 0

match opcao:
    case 1:
        print("\nIngresso Inteira")
    case 2:
        desconto = valor * 0.50
        print("\nIngresso Meia")
    case 3:
        desconto = valor * 0.30
        print("\nIngresso Promocional")
    case _:
        print("\nOpção inválida")


if opcao in [1, 2, 3]:
    valor_final = valor - desconto
    print(f"Valor final: R$ {valor_final:.2f}")