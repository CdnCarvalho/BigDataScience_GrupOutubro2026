produto1 = {} #dicionário vazio imprimi 2 chaves
# print(produto1)

produto = {
    'nome': 'Notebook',
    'preco': 3500,
    'marca': 'Lenovo', 
    # 'preco': 200 não pode repetir a chave
}

print(produto)
print(produto['marca'])  # Imprimi o valor da chave

produto['nome'] = 'Notebook A9' #trocando o valor da chave
print(produto)

produto['tela'] = '17"' #adiciona uma chave ao dicionário
print(produto)

del produto['marca'] #apaga a chave e o valor
print(produto)

print(produto.values())
print(produto.items())
print(produto.keys())

