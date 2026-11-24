lista_catalogo = []

for i in range(2):
    print(f"\nCadastro de Livro - {i+1}")
    livro = {}

    livro['titulo'] = input("Insira o título do livro: ")
    livro['ano'] = int(input("Insira o ano de publicação do livro: "))
    livro['genero'] = input("Insira o gênero do livro: ")
    lista_catalogo.append(livro)

#   if livro['ano'] >= 2020:   
    
for livro in lista_catalogo:
    if livro['ano'] >= 2020:
        print(livro)

        print(f'\nLIVROS À PARTIR DE 2020')
        print(livro)
        print(f'Título: {livro['titulo']}')
        print(f'Ano: {livro['ano']}') 
        print("Programa Encerrado")