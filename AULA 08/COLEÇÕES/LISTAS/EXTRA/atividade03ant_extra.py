# numeros = []
pares = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    # numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)

print("\nNúmeros pares:")
print(pares)