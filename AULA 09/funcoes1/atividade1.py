
def dobro(n):
    dobro = n * 2
    return dobro

def triplo(n):
    triplo = n * 3
    return triplo

def quadrado(n):
    quadr = n ** 2
    return quadr

num = int(input("Informe um número: "))
d = dobro(num)
t = triplo(num)
q = quadrado(num)

print(f'\nNúmero: {num}\nDobro: {d}\nTriplo: {t}\nQuadrado: {q}')

