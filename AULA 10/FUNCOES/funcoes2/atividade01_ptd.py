# Neste exemplo, o sistema foi desenvolvido para auxiliar no controle de peso de peixes durante uma fiscalização ambiental. 
# O programa solicita o peso total pescado e verifica se o valor ultrapassa o limite permitido pela regulamentação. 
# Caso exista excesso de peso, o sistema calcula automaticamente o valor da multa com base na quantidade excedente. 
# Para organizar melhor o código, o cálculo da multa foi separado em uma função específica.



# Função responsável por calcular o valor da multa
def calcula_multa(e):
    # Multiplica o peso excedente pelo valor da multa por quilo
    m = e * MULTA

    # A função retorna o valor total da multa calculada
    return m


# Constante:
# Abaixo fazemos o uso das constante. Elas são definidas em letras maiúsculas.
# As constantes são usadas para armazenar valores que não devem ser alterados 
# durante a execução do programa.

# Constante: Limite máximo permitido de peso pescado
LIMITE = 100

# Constante: Valor cobrado de multa por quilo excedente
# Valor cobrado de multa por quilo excedente
MULTA = 4.00


# Entrada de dados:
# O usuário informa o peso total pescado
peso = float(input('Informe o peso: '))


# Verifica se o peso informado ultrapassa o limite permitido
if peso > LIMITE:
    # Caso ultrapasse, Calcula o excesso de peso e chama a função calcula_multa()
    excedente = peso - LIMITE

    # Chamando a função calcula_multa(e)
    # O valor excedente é enviado para a função como parâmetro, isto é, dentro dos parênteses
    # A função calcula_multa(e) recebe o valor enviado e guarda na variável 'e' 
    # Faz o cálculo e retorna o valor da multa calculada como "m"
    vl_multa = calcula_multa(excedente)

    # Exibindo o valor da multa ao usuário
    print(f'Excesso de Peso. O valor da Multa é {vl_multa:.2f}')

else:

    # Caso o peso esteja dentro do limite permitido
    print(f'Sem multa à pagar. O peso pescado foi {peso:.2f} Kg')