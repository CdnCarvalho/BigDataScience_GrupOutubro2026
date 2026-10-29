
# Exemplo 1 — Calculando o valor de uma compra
# Crie um programa que solicite o preço de um produto e a quantidade comprada.
# Em seguida, calcule e mostre o valor total da compra.
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

print(f"Valor total da compra: R$ {total:.2f}")




# Exemplo 1 — Divisão de uma conta entre amigos
# Crie um programa que solicite o valor total de uma conta em um restaurante 
# e a quantidade de amigos que irão dividi-la. 
# O programa deverá calcular quanto cada amigo pagará e mostrar o resultado.
valor_conta = float(input("Digite o valor total da conta: R$ "))
amigos = int(input("Quantos amigos vão dividir a conta? "))

valor_por_pessoa = valor_conta / amigos

print(f"Cada amigo deverá pagar R$ {valor_por_pessoa:.2f}")




# Exemplo 2 — Cálculo do valor de uma corrida de táxi
# Uma empresa de táxi cobra uma taxa fixa de R$ 8,00 mais R$ 3,00 por 
# quilômetro percorrido. Ao final da corrida, é acrescentada uma taxa 
# de serviço de R$ 5,00, e o valor total é dividido igualmente entre os 
# passageiros. Crie um programa que solicite a distância percorrida e a 
# quantidade de passageiros, calcule o valor total da corrida e mostre 
# quanto cada passageiro deverá pagar.
distancia = float(input("Digite a distância percorrida em km: "))
passageiros = int(input("Digite a quantidade de passageiros: "))

valor_corrida = 8 + (distancia * 3)
valor_total = valor_corrida + 5
valor_por_passageiro = valor_total / passageiros

print(f"Valor total da corrida: R$ {valor_total:.2f}")
print(f"Valor por passageiro: R$ {valor_por_passageiro:.2f}")



# Desconto
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

subtotal = preco * quantidade
desconto = subtotal * 0.10
total = subtotal - desconto

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {total:.2f}")