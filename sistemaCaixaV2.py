
#criação das funções

def confirmar_compra():
    confirmar = input("Digite 'S/Enter' se deseja confirmar sua compra: ").lower()
    if confirmar in ["s", ""]:
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
        return True
    
    else:
        print("Pagamento cancelado.")
        return False

def obter_dados():

    print("-"*30)
    print("Sistema de Caixa")
    print("-"*30)
    global valor_produto
    while True:
        #obtendo dados da compra
        nome_produto = input("Insira o nome do produto: ")
        if nome_produto == "":
            print("O produto deve conter um nome para continuar.")
            continue
        valor_produto = input(f"Insira o valor de {nome_produto}: ")
        if valor_produto == "":
            print("O produto deve conter um valor para continuar.")
            continue
    
        print("-"*30)
        return conversao()
    #conversão 
def conversao():
    global valor_produto
    valor_produto = (valor_produto).replace(",",".") 
    
    try:
        if valor_produto == str:
            raise ValueError("valor invalido")
        valor_produto = float(valor_produto)
    except ValueError:
        print("Valor inserido invalido. Use numeros na hora de digitar o valor")
        return obter_dados()

    return sistema_compra()

    #Organizando forma de pagamento
def sistema_compra():

    global valor_produto

    print(f"O total da compra ficou em R${valor_produto:.2f}, qual a forma de pagamento? ")
    a = int(input("(1)Pix ou Dinheiro, (2)Credito a vista, (3)Credito em 2x, (4)Credito em 3x ou mais: "))
    print("-"*30)

    if a == 1:
        valor_produto = valor_produto * 0.85
        print(f"O valor total da compra ficou em R${valor_produto:.2f}. Pagamneto no pix ou em dinheiro recebem 15 por cento de desconto")
        print("-"*30) 
        
    elif a == 2:
        valor_produto = valor_produto * 0.90
        print(f"O valor total da compra ficou em R${valor_produto:.2f}. Pagamneto no credito a vista recebem 10 por cento de desconto")
        print("-"*30) 

    elif a == 3:
        valor_produto = valor_produto /2
        print(f"O total da compra ficou em 2 parcelas de R${valor_produto:.2f} sem juros")
        print("-"*30) 

    elif a ==4:
        parcelas = int(input("Insira o numero de vezes que o cliente deseja dividir, com o maximo de 12 vezes: "))
        valor_produto = valor_produto *1.10
        valor_produto = valor_produto/ parcelas
        print(f"O total da compra ficou em {parcelas} parcelas de R${valor_produto:.2f}, com juros de 10 por cento ao total da compra")
        print("-"*30) 

    else:
        print("Insira uma forma de pagamento valida para continuar!")

    confirmar_compra()

#maneira de iniciar e manter o sistema o sistema rodando
while True:
    obter_dados()
    sair =input("Digite 'S' caso queira sair do sistema, se não, so aperte enter: ").lower()
    
    if sair == "s":
        print("até logo")
        print("-"*30)
        break
    
        
