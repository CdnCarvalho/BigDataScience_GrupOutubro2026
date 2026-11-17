
# 1. Criando um conjunto
frutas = {"Maçã", "Banana", "Laranja", "Uva"}
print(frutas)

# 2. Eliminando elementos duplicados
numeros = {10, 20, 10, 30, 20, 40}
print(numeros)

# 3. Percorrendo um conjunto
for fruta in frutas:
    print(fruta)

# 4. Adicionando elementos
frutas.add("Morango")
print(frutas)

# 5. Removendo elementos com remove()
frutas.remove("Banana")
print(frutas)

# 6. Removendo elementos com discard()
frutas.discard("Uva")
print(frutas)

# 7. Verificando se um elemento existe
if "Maçã" in frutas:
    print("Fruta encontrada!")
else:
    print("Fruta não encontrada!")

# 8. Verificando a quantidade de elementos
print(f"Quantidade de frutas: {len(frutas)}")

# 9. União de conjuntos
turma_a = {"Ana", "Pedro", "João"}
turma_b = {"Maria", "Pedro", "Carlos"}
todos_alunos = turma_a.union(turma_b)
print(todos_alunos)

# 10. Interseção de conjuntos
turma_a = {"Ana", "Pedro", "João"}
turma_b = {"Maria", "Pedro", "João"}
alunos_em_comum = turma_a.intersection(turma_b)
print(alunos_em_comum)

# 11. Diferença entre conjuntos
turma_a = {"Ana", "Pedro", "João"}
turma_b = {"Maria", "Pedro", "Carlos"}
resultado = turma_a.difference(turma_b)
print(resultado)

# 12. Convertendo lista em conjunto
vendas = [100, 200, 100, 300, 200, 400]
vendas_unicas = set(vendas)
print(vendas_unicas)

# 13. Criando um conjunto vazio
numeros = set()
numeros.add(10)
numeros.add(20)
print(numeros)
