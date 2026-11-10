numero = float(input("Insira um número: ")) 

print() 

match numero: 
    case numero if numero > 0: 
        print(f'Número {numero} é positivo!') 

    case numero if numero < 0: 
        print(f'Número {numero} é negativo') 

    case _: 
        print("Número 0") 

 

print("Fim do Programa!") 