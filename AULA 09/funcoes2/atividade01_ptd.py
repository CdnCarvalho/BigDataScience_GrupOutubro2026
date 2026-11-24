# Neste exemplo, o sistema foi desenvolvido para auxiliar no controle de
#  peso de peixes durante uma fiscalização ambiental. 
# O programa solicita o peso total pescado e verifica se o valor 
# ultrapassa o limite permitido pela regulamentação. 
# Caso exista excesso de peso, o sistema calcula automaticamente
#  o valor da multa com base na quantidade excedente. 
# Para organizar melhor o código, o cálculo da multa foi separado 
# em uma função específica.


# Função responsável por calcular o valor da multa
def calcula_multa(e):
    m = e * MULTA  # Excedente vezes multa
    return m  # Retorna a multa


# Constante: Limite máximo permitido de peso pescado
LIMITE = 100
MULTA = 4.00

peso = float(input('Informe o peso pescado: '))

# Verifica se o peso informado ultrapassa o limite permitido
if peso > LIMITE:
    excedente = peso - LIMITE

    vl_multa = calcula_multa(excedente)
    print(f'Excesso de Peso. O valor da Multa é {vl_multa:.2f}')

else:
    print(f'Sem multa à pagar. O peso pescado foi {peso:.2f} Kg')