# É uma coleção mutável.
# Não permite elementos duplicados.
# Não garante a ordem dos elementos.
# Não permite acesso por índices.

# Criando um conjunto vazio
dias = set()
dias.add('segunda')
dias.add('terça')
print(dias)

# 1. Conjuntos set
frutas = {"Maçã", "Banana", "Laranja", "Uva"}
print(frutas)


# 4. Adicionando elementos
frutas.add("Morango")
print(frutas)

# 5. Removendo elementos com remove()
frutas.remove("Banana")
print(frutas)

# 6. Removendo elementos com discard()
frutas.discard("Uva")
print(frutas)

# 8. Verificando a quantidade de elementos
print(f"Quantidade de frutas: {len(frutas)}")

conjunto = {1, 2, 3, 4}
print(sum(conjunto))

# 12. Convertendo lista em conjunto
vendas = [100, 200, 100, 300, 200, 400]
vendas_unicas = set(vendas)
print(vendas_unicas)

# Percorrendo um conjunto
for fruta in frutas:
    print(fruta)

# 7. Verificando se um elemento existe
if "Maçã" in frutas:
    print("Fruta encontrada!")
else:
    print("Fruta não encontrada!")




