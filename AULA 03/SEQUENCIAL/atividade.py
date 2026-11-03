# ATIVIDADE 1 - Aumento de salário
# Crie um programa que solicite o salário atual de um funcionário. 
# Em seguida, calcule um aumento de 15% sobre o salário e apresente 
# o valor do aumento e o novo salário do funcionário após o reajuste.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)


#  ############### ATIVIDADES PDT #################
# ATIVIDADE 2 — Boletim escolar
# Criar duas variáveis com as notas
nota1 = 6.0
nota2 = 9.0

# Calcular a média e guardar em uma terceira variável
media = (nota1 + nota2) / 2

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)



# ATIVIDADE 3 — Calculadora com input
# Receber dois números do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Calcular e guardar as operações
soma      = n1 + n2
subtracao = n1 - n2
produto   = n1 * n2
divisao   = n1 / n2

# Exibir os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", produto)
print("Divisão:", divisao)
