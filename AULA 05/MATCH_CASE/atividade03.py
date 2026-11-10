# # ATIVIDADE 02 

# Escreva um algoritmo em Python, que receba um valor monetário 
# de venda fornecido pelo usuário e classifique esta venda 
# de acordo com as seguintes regras: 

# Venda pequena: Valores inferiores a 100. 
# Venda média: Valores entre 100 (inclusivo) e 500 (exclusivo).  
# Venda grande: Valores iguais ou superiores a 500. 

valor = float(input("Insira o valor da compra: "))

match valor:
    case vlr if valor < 100:
        print("Venda pequena")
    
    case vlr if valor < 500:
        print("Valor Médio")

    case _:
        print("Valor Grade")
        