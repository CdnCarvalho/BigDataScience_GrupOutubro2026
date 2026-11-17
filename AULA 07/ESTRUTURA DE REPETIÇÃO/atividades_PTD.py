# ATIVIDADE 1 - 
# Notas de 10 alunos (Versão 1 FOR)
for aluno in range(10): 
    print(f"\n---- Aluno {aluno + 1} ----") 
    # soma_notas = 0  

    n1 = float(input(f"Digite a nota Nota 1: ")) 
    n2 = float(input(f"Digite a nota Nota 2: "))
    n3 = float(input(f"Digite a nota Nota 3: "))
    n4 = float(input(f"Digite a nota Nota 4: "))
    
    media_final = (n1 + n2 + n3 + n4) / 4  # acumula a soma das notas

    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais

# ---------------------------------------------------------------------

# ATIVIDADE 1 
# VERSÃO 2 - Usando 4 variáveis e apenas 1 FOR
for aluno in range(10): 
    print(f"\n---- Aluno {aluno + 1} ----")  
    soma_notas = 0 

    for nota in range(4):
        valor_nota = float(input(f"Digite a nota {nota + 1}: "))  
        soma_notas += valor_nota 

    media_final = soma_notas / 4  
    print(f"A média final do aluno {aluno + 1} é: {media_final:.2f}")  # exibe a média com 2 casas decimais

# -------------------------------------------------------------------------------------------------------------



# ATIVIDADE EXTRA
# Algoritmo que recebe 10 valores de vendas e calucula o mostra o valor normal # da venda, o valor 
# do desconto e o valor total a ser pago, considerando, que vendas acima de R$ 1000,00 tem desconto de 10%.

for venda in range(3):  
    print(f"\n---- Venda {venda + 1} ----") 
    valor_venda = float(input(f"Digite o valor da venda: ")) 
    desconto = 0  
    # novo_valor = valor_venda  
    
    if valor_venda > 1000:
        desconto = valor_venda * 0.10  
        valor_total = valor_venda - desconto 
    else:
        valor_total = valor_venda

    print(f"Valor da venda: R$ {valor_venda:.2f}")  
    print(f"Desconto: R$ {desconto:.2f}") 
    print(f"Total a Pagar: R$ {valor_total:.2f}") 
# -------------------------------------------------------------------------------------------------------------
