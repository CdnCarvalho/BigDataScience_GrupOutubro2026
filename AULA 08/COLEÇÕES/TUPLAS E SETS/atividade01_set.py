numeros = []

for i in range(15):
    numero = int(input('Informe um número: '))
    numeros.append(numero)

sem_duplicados = set(numeros)

print(f'Números informados: {numeros}')
print(f'Números sem duplicidade: {sem_duplicados}')


# Versão 02
# ------------------------------------------------------
# adicionando em sets()
numeros = set()

for i in range(15):
    numero = int(input('Informe um número: '))
    numeros.add(numero)
