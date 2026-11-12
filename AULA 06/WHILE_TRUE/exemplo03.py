# Se não sabemo quantas vezes precisaremos fazer isso, usando while True?
# usando while true
while True:
    numero = int(input('\nDigite um número: '))

    if numero != 0:  
        # Se, só puder positivos maiores que 0 (if numero > 0)
        dobro = numero * 2
        triplo = numero * 3
        quadrado = numero ** 2

        print(f'O dobro de {numero} é {dobro}')
        print(f'O triplo de {numero} é {triplo}')
        print(f'O quadrado de {numero} é {quadrado}')
    else:
        print('Você digitou zero!')

    resposta = input('\nQuer continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
# ----------------------------------------------------------------------------------

