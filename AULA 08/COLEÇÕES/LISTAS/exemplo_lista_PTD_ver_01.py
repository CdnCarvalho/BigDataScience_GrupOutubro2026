META = 1000
META_MINIMA = 700

for i in range(10):
    print(f"\nVENDEDOR {i+1}")

    qtd = int(input("Quantidade de vendas: "))

    vendas = []

    for n in range(qtd):
        valor = float(input(f"Digite o valor da venda {n+1} R$: "))
        vendas.append(valor)

    total = sum(vendas)
    media = total / qtd

    print(f"\nTotal vendido: R$ {total:.2f}")
    print(f"Média das vendas: R$ {media:.2f}")

    if media >= META:
        print(f"Meta de R$ {META} atingida.")

    elif media >= META_MINIMA:
        print(f"Bateu a meta mínima de R$ {META_MINIMA}.")

    else:
        print("Abaixo das metas.")