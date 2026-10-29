# EXEMPLO 1 - IF / ELSE básico
# Enunciado: Verifique se a pessoa é maior de idade.
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# -----------------------------------------------------------


# EXEMPLO 2 - IF / ELSE
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - ano_nascimento

if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade.")
else:
    print(f"Você tem {idade} anos e é menor de idade.")
# -----------------------------------------------------------



# EXEMPLO 2 - IF com ELIF
# Enunciado: Verifique a faixa de pontuação de um jogador.
pontos = int(input("Digite sua pontuação: "))

if pontos >= 100:
    total = pontos + 10
    print(f"Excelente! Bônus adicionado. Agora você tem {total} pontos.")
elif pontos >= 50:
    total = pontos + 5
    print(f"Bom desempenho! Bônus adicionado. Agora você tem {total} pontos.")
else:
    print(f"Você está começando, pratique mais! Sua pontuação foi de: {pontos}")
# -----------------------------------------------------------