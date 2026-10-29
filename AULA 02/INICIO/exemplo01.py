# Roteiro de aula — Entrada de dados, tipos de variáveis e operadores aritméticos em Python

## 1. Entrada de dados com input()
# Recebendo e exibindo um nome
nome = 'João'
ano_atual = 2026
ano_nascimento = 2002
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")

# alterando p/ input()
ano_atual = 2026
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos")




## 2. Variáveis e tipos de dados
# str - Texto
nome = "Carlos"

# int - Número inteiro
idade = 20

# float - Número decimal
preco = 15.50



# Verificando os tipos das variáveis
print(type(nome))
print(type(idade))
print(type(preco))



## 3. Conversão de dados com int() e float()
# Recebendo um número inteiro
idade = int(input("Digite sua idade: "))
print(idade)

# Recebendo um número decimal
preco = float(input("Digite o preço do produto: R$ "))
print(preco)


## 4. Operadores aritméticos
# Definindo os números
numero1 = 10
numero2 = 5

# Adição
print(numero1 + numero2)

# Subtração
print(numero1 - numero2)

# Multiplicação
print(numero1 * numero2)

# Divisão
print(numero1 / numero2)


## 5. Primeiro cálculo com entrada de dados


# Calculando o valor total de uma compra
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco * quantidade

print(f"Valor total da compra: R$ {total:.2f}")
