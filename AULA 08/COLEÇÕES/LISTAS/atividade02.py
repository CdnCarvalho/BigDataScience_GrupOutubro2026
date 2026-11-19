numeros = []

while True:
    valor = input('Informe um número ou N para encerrar: ')

    if valor.upper() == 'N':
        break

    numeros.append(int(valor))

print(f'Quantidade de números informados: {len(numeros)}')