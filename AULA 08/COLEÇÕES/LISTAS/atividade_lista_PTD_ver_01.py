QUANTIDADE_ESTUDANTES = 5

for i in range(QUANTIDADE_ESTUDANTES):
    print(f"\nESTUDANTE {i+1}")

    notas = []

    for n in range(4):
        nota = float(input(f"Digite a {n+1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / len(notas)

    if media >= 7:
        print(f"Aprovado, média: {media:.2f}")
    else:
        print(f"Reprovado, média: {media:.2f}")