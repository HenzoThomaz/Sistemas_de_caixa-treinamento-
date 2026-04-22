
#criação das funções

def confirmar_compra():
    confirmar = input("Digite 'S/Enter' se deseja confirmar sua compra: ").lower()
    if confirmar in ["s", ""]:
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
        
    else: 
        print("Pagamento cancelado.")

    print("-"*30)

def sistema_compra():

    print("-"*30)
    print("Sistema de Caixa")
    print("-"*30)

    #obtendo dados da compra
    nome_produto = input("Insira o nome do produto: ")
    valor_produto= input(f"Insira o valor de {nome_produto}: ")
    print("-"*30)
    #conversão 
    valor_produto = (valor_produto).replace(",",".") 
    valor_produto = float(valor_produto)

    #Organizando forma de pagamento

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
    sistema_compra()
    sair =input("Digite 'S' caso queira sair do sistema, se não, so aperte enter: ").lower()
    print("-"*30)
    if sair == "s":
        print("até logo")
        break
    
        
