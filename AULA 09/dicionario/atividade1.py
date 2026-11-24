
cadastro = []

for i in range(5):
    print(f'\nCadastro de Contatos - {i+1}')
    contato = {}

    contato['nome_completo'] = input("Insira o nome completo do contato:  ")
    contato['telefone'] = input("Insira o telefone:  ")
    contato['email'] = input("Insira o e-mail: ")

    cadastro.append(contato)
    print(cadastro)

print('-'*90)
for pessoa in cadastro:
    # print(pessoa)
    print(pessoa['email'])