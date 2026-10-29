
# 01 - Elabore um programa que imprima na tela a seguinte 
# frase `Análise de Dados em Python`
# -------------------------------------------------------------------------------------


# 02 - Elabore um programa que escreve seu nome na primeira linha, 
# o bairro na segunda e a profissão na terceira.  

# EXEMMPLO
# Nome: Bruno Fabri
# Endereço: Rua ABC
# CEP: 002220-010
# 
# -------------------------------------------------------------------------------------
# Atualize para que o algoritmo pergunte o nome, endereço e CEP do usuário e imprima na tela.



# Atividade 1 — Compra de refrigerantes
# Você foi ao mercado comprar refrigerantes para uma reunião com amigos.
# Crie um programa que solicite o preço de uma unidade e a quantidade comprada. 
# Ao final, calcule e mostre o valor total da compra.
preco = float(input("Digite o preço do refrigerante: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

print(f"Valor total da compra: R$ {total:.2f}")




# Atividade 2 — Divisão da conta da pizzaria
# Você e seus amigos foram a uma pizzaria. A conta ficou em R$ 120,00, 
# e todos decidiram dividir o valor igualmente. Crie um programa que solicite a 
# quantidade de pessoas e calcule quanto cada uma deverá pagar.
valor_conta = 120.00

pessoas = int(input("Quantas pessoas vão dividir a conta? "))

valor_por_pessoa = valor_conta / pessoas

print(f"Cada pessoa deverá pagar R$ {valor_por_pessoa:.2f}")




# ATIVIDADE  - Aumento de salário
# Atividade — Cálculo de aumento salarial
# Crie um programa que solicite o salário atual de um funcionário. 
# Em seguida, calcule um aumento de 15% sobre o salário e apresente 
# o valor do aumento e o novo salário do funcionário após o reajuste.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)




#  ############### ATIVIDADES PDT #################

# ATIVIDADE 1 — Boletim escolar
# Criar duas variáveis com as notas
nota1 = 6.0
nota2 = 9.0

# Calcular a média e guardar em uma terceira variável
media = (nota1 + nota2) / 2

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)



# ATIVIDADE 2 — Calculadora com input
# Receber dois números do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Calcular e guardar as operações
soma      = n1 + n2
subtracao = n1 - n2
produto   = n1 * n2
divisao   = n1 / n2
modulo    = n1 % n2

# Exibir os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", produto)
print("Divisão:", divisao)
print("Módulo:", modulo)