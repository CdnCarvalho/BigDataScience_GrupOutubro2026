numeros = []

for i in range(12):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

print(f'Números em ordem crescente: {sorted(numeros)}')