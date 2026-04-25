print("-"*30)
print("Sistema de Caixa")
print("-"*30)

#obtendo dados da compra
nome_produto = input("Insira o nome do produto: ")
valor_produto= input(f"Insira o valor de {nome_produto}: ")
print("-"*30)

#conversão meio porca
valor_produto = (valor_produto).replace(",",".") #verificar se isso funciona
valor_produto = float(valor_produto)
#Organizando forma de pagamento

print(f"O total da compra ficou em R${valor_produto:.2f}, qual a forma de pagamento? ")
a = int(input("(1)Pix ou Dinheiro, (2)Credito a vista, (3)Credito em 2x, (4)Credito em 3x ou mais: "))
print("-"*30)

if a == 1:
    valor_produto = valor_produto * 0.85
    print(f"O valor total da compra ficou em R${valor_produto:.2f}. Pagamneto no pix ou em dinheiro recebem 15 por cento de desconto")
    confirm = input("Digite 'S' se deseja continuar: ").lower()
    print("-"*30)
    if confirm == "s" or confirm == "":
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
    else:
        print("Pagamento cancelado.")
        
elif a == 2:
    valor_produto = valor_produto * 0.90
    print(f"O valor total da compra ficou em R${valor_produto:.2f}. Pagamneto no credito a vista recebem 10 por cento de desconto")
    confirm = input("Digite 'S' se deseja continuar: ").lower()
    print("-"*30)
    if confirm == "s" or confirm == "":
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
    else:
        print("Pagamento cancelado.")
#problema

elif a == 3:
    valor_produto = valor_produto /2
    print(f"O total da compra ficou em 2 parcelas de R${valor_produto:.2f} sem juros")
    confirm = input("Digite 'S' se deseja continuar: ").lower()
    print("-"*30)
    if confirm == "s" or confirm == "":
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
    else:
        print("Pagamento cancelado.")

elif a ==4:
    parcelas = int(input("Insira o numero de vezes que o cliente deseja dividir, com o maximo de 12 vezes: "))
    valor_produto = valor_produto *1.10
    valor_produto = valor_produto/ parcelas
    print(f"O total da compra ficou em {parcelas} parcelas de R${valor_produto}, com juros de 10 por cento ao total da compra")
    confirm = input("Digite 'S' se deseja continuar: ").lower()
    print("-"*30)
    if confirm == "s" or confirm == "":
        print("Pagamento confirmado, obrigado por comprar conosco, e volte sempre!!")
    else:
        print("Pagamento cancelado.")

else:
    print("Insira uma forma de pagamento valida para continuar!")

print("-"*30)

"""TODO versão v2: deve conter a criação de funções, uma para confirmar pagamento, e outra caso deseja adicionar outros itens individualmente, ou seja repetir o sitema
TODO adicionar um carrinho de compras, uma função que armazene todos os produtos do usuario em listas e no final escolha o pagamento, transformar cada forma de pagamneto em uma função e so chamar-la, controlar o fluxo de codico chamando as funções manualmnete, ao invez de acarretar uma na outra, retornar variaveis ao final e nao usar mais o global, mais detalhes são livres
"""

