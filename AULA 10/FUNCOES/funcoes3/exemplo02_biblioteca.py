# ##### EXEMPLO 02

import random
import subprocess  # Utilizar ao invés de os.system()
# import os - O os.system() está ficando depreciado

def calcula_dobro(n):
    return n * 2


def calcula_triplo(n): 
    return n * 3


def calcula_quadrado(n):
    return n ** 2


def calcula_metade(n):
    return n / 2



# Algoritmo que usuário informa dois números e escolhe se quer o dobro, ou triplo, ou o quadrado 
# Pedir para criar a função calcular a metade.

subprocess.run('cls', shell=True)
n = random.randint(1, 100)
# n = int(input('Informe o número: '))

print('\n ###### MENU DE OPÇÕES ######')
print(30*'=')
print('[1] - Dobro\n[2] - Triplo\n[3] - Quadrado \n[4] - Metade')

print(f'\nValor sorteado: {n}')
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