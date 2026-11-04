print('''
[1] - Marketing
[2] - Financeiro
[3 a 5] - Adm
[6 a 9] - TI
[10 a 20] - Serviços Gerais
''')

escolha = int(input("Escolha uma opção: "))

match escolha:
    
    case 1:
        print('Marketing')
    
    case 2:
        print("Financeiro")
    
    case 3 | 4 | 5:
        print("Adm")
    
    case numero if 6 <= numero <= 9:
        print("TI")
    
    case numero if 10 <= numero <= 20:
        print("Serviços Gerais")

    case _:
        print("Escolha inválida")

# -------------------------------------------------------------------



# EXEMPLO 02 - IDADE (SE PRECISAR)
print('''
CLASSIFICAÇÃO DE IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos
''')

idade = float(input('Informe a sua idade:'))

match idade:
    case i if i < 12:
        print('Criança')
    case i if i < 18: 
        print('Adolescente')
    case i if i >= 18:
        print('Adulto')
    case _:
        print('Opção inválida!')


# #####  OUTRA FORMA 
print('''
CLASSIFICAÇÃO DE IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos
''')

idade = float(input('Informe a sua idade:'))

match idade:
    case i if 0 <= i < 12:
        print('Criança')
    case i if 12 <= i < 18: 
        print('Adolescente')
    case i if i >= 18:
        print('Adulto')
    case _:
        print('Opção inválida!')

# -------------------------------------------------------------------