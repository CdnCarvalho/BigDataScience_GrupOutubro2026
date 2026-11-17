# Criação da lista
produtos = []

# Cadastro de 5 produtos
for i in range(5):
    produto = input(f"Digite o nome do produto {i + 1}: ")
    produtos.append(produto)

# Exibição da lista
print("\nProdutos cadastrados:")
print(produtos)

# Acesso a um elemento
n = int(input("\nInforme a posição do produto que deseja acessar: "))
if n in range(5):
    print(f'Produto {n}: {produtos[n - 1]}')


# Alteração de um elemento
produtos[n-1] = input(f"\nAltere o nome produto {n}: ")
print(produtos)

# Inclusão de um elemento
novo_produto = input("\nCadastre um novo produto: ")
produtos.append(novo_produto)
print(produtos)

# Remoção de um elemento
produto_a_remover = input("\nDigite o produto que deseja remover: ")
produtos.remove(produto_a_remover)
print(produtos)

# Lista atualizada
print("\nLista atualizada:")
print(produtos)

print('\nOperação finalizada')