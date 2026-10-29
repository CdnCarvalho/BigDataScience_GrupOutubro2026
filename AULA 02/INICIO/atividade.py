
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







# ATIVIDADE  - Aumento de salário
# Enunciado: Calcule o novo salário de um funcionário com aumento de 15%.
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