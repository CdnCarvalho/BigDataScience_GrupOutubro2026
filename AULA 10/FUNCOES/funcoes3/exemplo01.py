# ##### EXEMPLO 02
def calcula_dobro(n):
    return n * 2


def calcula_triplo(n): 
    return n * 3


def calcula_quadrado(n):
    return n ** 2


def calcula_metade(n):
    return n / 2


# Algoritmo que usuário informa dois números e escolhe se quer o dobro, ou triplo, ou o quadrado 
# calcular a metade
n = int(input('Informe o número: '))

print('\n ###### MENU DE OPÇÕES ######')
print(30*'=')
print('[1] - Dobro\n[2] - Triplo\n[3] - Quadrado - \n[4] - Metade')

opcao = int(input('\nDigite a opção desejada: '))

match opcao:
    case 1:
        reposta = calcula_dobro(n)
    case 2:
        reposta = calcula_triplo(n)
    case 3:
        reposta = calcula_quadrado(n)
    case 4:
        reposta = calcula_metade(n)  # pedir depois
    case _:
        reposta = 'Opção inválida'

print(f'Resultado: {reposta}')
# pedir para dar mais uma opção: calcular a metade