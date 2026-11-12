
# Se não sabemo quantas vezes precisaremos fazer isso, sem usar while True?
resposta = 'S'
while resposta == 'S':  # resposta != 'N'
    numero = int(input('\nDigite um número: '))
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f'O dobro de {numero} é {dobro}')
    print(f'O triplo de {numero} é {triplo}')
    print(f'O quadrado de {numero} é {quadrado}')
    
    resposta = input('\nQuer continuar? [S/N]: ').upper()
# ----------------------------------------------------------------------------------

