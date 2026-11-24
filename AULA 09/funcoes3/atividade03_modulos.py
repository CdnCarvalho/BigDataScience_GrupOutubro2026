# ATIVIDADE 03 - MODULOS
import random
import subprocess  # Utilizar ao invés de os.system()
# import os - O os.system() está ficando depreciado

# importar as funçoes
from auxiliar.operacoes_basicas import calcula_somar, calcula_subtrair, calcula_multiplicar, calcula_dividir


# Início
subprocess.run('cls', shell=True)
n1 = random.randint(10, 100)
n2 = random.randint(1, 10)

print(f'Os números sorteados foram {n1} e {n2}')

print('\nEscolha uma operação: ')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')


# match case
opcao = int(input('\nDigite a opção desejada: '))
match opcao:
  case 1:
    print('Você escolheu somar')
    print(calcula_somar(n1, n2))

  case 2:
    print('Você escolheu subtrair')
    print(calcula_subtrair(n1, n2))

  case 3:
    print('Você escolheu multiplicar')
    print(calcula_multiplicar(n1, n2))

  case 4:
    print('Você escolheu dividir')
    print(calcula_dividir(n1, n2))

  case _:
    print('Opção inválida')