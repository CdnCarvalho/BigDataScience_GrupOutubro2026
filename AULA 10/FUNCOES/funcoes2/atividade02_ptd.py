def calcula_imc(p, a):
    i = p / a**2
    return i


while True:
    print('\nNovo Cálculo IMC')

    peso = float(input('Informe o peso: '))
    altura = float(input('Informe a altura: '))

    imc = calcula_imc(peso, altura)

    print(f'\nIMC: {imc}')

    # Classificação do IMC
    match imc:
        case i if i < 17:
            print('Muito abaixo do peso.')
        case i if i < 18.5:
            print('Abaixo do peso.')
        case i if i < 25:
            print('Peso Normal.')
        case i if i < 30:
            print('Acima do peso.')
        case i if i < 35:
            print('Obesidade Grau I.')
        case i if i <= 40:
            print('Obesidade Grau II.')
        case i if i > 40:
            print('Obesidade Grau III.')

   
    # Condição de Parada do Loop
    continuar = input('\nDeseja continuar? [S/N]: ').strip().upper()
    
    if continuar != 'S':
        break

