# ATIVIDADE 01
nota = float(input("Digite a nota final: "))
frequencia = float(input("Digite a frequência (%): "))
mensalidade = float(input("Digite o valor da mensalidade: "))

if nota >= 7 and frequencia >= 75:
    bolsa = mensalidade * 0.20
    print(f"O aluno recebe uma bolsa de R$ {bolsa:.2f}")
else:
    print("O aluno não tem direito à bolsa.")
# ---------------------------------------------------------------------


# ATIVIDADE 02
valor_compra = float(input("Digite o valor da compra: R$ "))
cadastrado = input("O cliente é cadastrado no programa de fidelidade? (s/n): ")

if valor_compra > 200 or cadastrado == "s":
    valor_final = valor_compra
    print(f"Frete grátis! Valor final: R$ {valor_final:.2f}")
else:
    valor_final = valor_compra + 25
    print(f"Frete de R$ 25,00. Valor final: R$ {valor_final:.2f}")
# ---------------------------------------------------------------------




# ATIVIDADE 03
# Entrada dos dados
valor = float(input("Informe o valor da compra: R$ "))
forma_pagamento = input("Informe a forma de pagamento (à vista ou parcelado): ").strip()

# Padronizando o texto para evitar erro de digitação
forma_pagamento = forma_pagamento.upper()

# Verificação das duas condições ao mesmo tempo
if valor > 250 and forma_pagamento == "PIX":
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")
# --------------------------------------------------------------------------





# ATIVIDADE 04
# Sistema para verificar se um cooperado/a tem acesso ao benefício

# Entrada de dados
tempo_filiacao = int(input("Informe o tempo de filiação (em anos): "))
valor_movimentado = float(input("Informe o valor movimentado nos últimos 6 meses (em R$): "))

# Verificação de pelo menos uma condição verdadeira (OR)
if tempo_filiacao > 3 or valor_movimentado > 5000:
    print("Você tem direito ao benefício especial da cooperativa.")
else:
    print("Você ainda não atende aos critérios para o benefício.")
# --------------------------------------------------------------------------