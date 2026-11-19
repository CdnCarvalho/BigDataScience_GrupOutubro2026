# É uma coleção imutável.
# Permite elementos duplicados.
# Mantém a ordem de inserção dos elementos.
# Permite acesso aos elementos por índices.
# Não permite adicionar, remover ou alterar elementos.

# 1. Criando uma tupla
frutas = ("Maçã", "Banana", "Laranja", "Uva")
print(frutas)

# 2. Acessando elementos
print(frutas[0])
print(frutas[2])
print(frutas[-1])

# 4. Verificando a quantidade de elementos
print(f"Quantidade de frutas: {len(frutas)}")

# 6. Contando ocorrências
numeros = (10, 20, 10, 30, 10, 40)
print(numeros.count(10))


# 7. Descobrindo a posição de um elemento
print(frutas.index("Laranja"))

# 8. Tupla com um único elemento
cidade = ("Niterói",)
print(type(cidade))

# 9. Convertendo tupla em lista, alterando e convertendo novamente
lista_frutas = list(frutas)
print(lista_frutas)


# 3. Percorrendo uma tupla
for fruta in frutas:
    print(fruta)


# 5. Verificando se um elemento existe
if "Banana" in frutas:
    print("Fruta encontrada!")
else:
    print("Fruta não encontrada!")