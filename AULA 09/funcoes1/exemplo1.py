# Funções sem parâmetros
def saudacao():
    print("\nOlá, como vai?")


saudacao()
# -----------------------------------------------


# Funções com parâmetros
def saudacao2(nome):
    print(f'\nOlá, {nome}!')


saudacao2("Maria")
saudacao2("Pedro")

nome = input("Insira o nome: ")
saudacao2(nome)
#------------------------------------------------



# Função que soma dois números informados pelo usuário
def soma(a, b):
    print(f'{a} + {b}')
    r = a + b
    return r


total = soma(5,9)
print(total)


# ----------------------------------------------
for i in range (3):
    n1 = int(input("\nInforme um número: "))
    n2 = int(input("Informe outro número: "))
    
    resposta = soma(n1,n2)
    print(f'Soma é: {resposta}')
