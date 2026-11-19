# Criação da lista
cidades = []

# Cadastro de 5 cidades
for i in range(5):
    cidade = input(f"Digite o nome da cidade {i + 1}: ")
    cidades.append(cidade)

# Exibição das cidades
print("\nCidades cadastradas:")
print(cidades)

# Exibição da terceira cidade
print(f"\nTerceira cidade: {cidades[2]}")

# Alteração da segunda cidade
cidades[1] = input("\nDigite o novo nome para a segunda cidade: ")
print(cidades)

# Inclusão de uma nova cidade
nova_cidade = input("\nDigite uma nova cidade: ")
cidades.append(nova_cidade)
print(cidades)

# Remoção de uma cidade
cidade_remover = input("\nDigite o nome da cidade que deseja remover: ")
if cidade_remover in cidades:
    cidades.remove(cidade_remover)
print(cidades)

# Exibição da lista atualizada
print("\nLista atualizada:")
print(cidades)