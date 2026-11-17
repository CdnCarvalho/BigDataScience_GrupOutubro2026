
# 1. Criando uma tupla
frutas = ("Maçã", "Banana", "Laranja", "Uva")
print(frutas)

# 2. Acessando elementos
print(frutas[0])
print(frutas[2])
print(frutas[-1])

# 3. Percorrendo uma tupla
for fruta in frutas:
    print(fruta)

# 4. Verificando a quantidade de elementos
print(f"Quantidade de frutas: {len(frutas)}")

# 5. Verificando se um elemento existe
if "Banana" in frutas:
    print("Fruta encontrada!")
else:
    print("Fruta não encontrada!")

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
lista_frutas[1] = "Morango"
frutas = tuple(lista_frutas)
print(frutas)
