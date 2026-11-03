# EXEMPLO 01 - IF com operador AND
# Enunciado: Verifique se o usuário pode realizar o login.
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha incorretos.")
# -----------------------------------------------------------


# EXEMPLO 02 - Combinação de condições com AND e OR
# Enunciado: Verifique se o cliente tem direito a um brinde.
compra = float(input("Digite o valor da compra: "))
cliente_frequente = input("O cliente é cadastrado no programa de fidelidade? (s/n): ").strip().lower()[0]
print(cliente_frequente)
if compra > 100 or cliente_frequente == "s":
    print("Cliente tem direito a um brinde!")
else:
    print("Sem brinde desta vez.")
# -----------------------------------------------------------


# EXEMPLO 03 - Combinação de condições com AND e OR
valor_pedido = float(input("Digite o valor do pedido: R$ "))
distancia = float(input("Digite a distância até sua casa em km: "))

if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    print("Você ganhou frete grátis.")
    print(f"Valor final: R$ {valor_final:.2f}")
else:
    valor_final = valor_pedido + 8
    print("Você pagará frete de R$ 8,00.")
    print(f"Valor final: R$ {valor_final:.2f}")



# EXEMMPLO 04
valor_recarga = float(input("Digite o valor da recarga: R$ "))
tempo_cliente = int(input("Há quantos anos você é cliente? "))

if valor_recarga >= 30 or tempo_cliente > 1:
    bonus = valor_recarga * 0.10
    total = valor_recarga + bonus
    print(f"Bônus: R$ {bonus:.2f}")
    print(f"Total disponível: R$ {total:.2f}")
else:
    total = valor_recarga
    print(f"Sem bônus. Total disponível: R$ {total:.2f}")