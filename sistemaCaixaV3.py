#dados e variaveis globais
estoque = {
    1: {"nome": "Teclado Mecânico", "preco": 150.00},
    2: {"nome": "Mouse Gamer", "preco": 80.00},
    3: {"nome": "Monitor 24'", "preco": 850.00},
    4: {"nome": "Headset Bluetooth", "preco": 200.00},
    5: {"nome": "Webcam HD", "preco": 120.00},
    6: {"nome": "Cabo HDMI 2m", "preco": 35.00},
    7: {"nome": "Mousepad Extra Large", "preco": 50.00},
    8: {"nome": "Suporte para Notebook", "preco": 45.00},
    9: {"nome": "Pendrive 64GB", "preco": 40.00},
    10: {"nome": "SSD 480GB", "preco": 280.00}
}

#Criação das funções

#função que chama um menu que mostrara os itens disponiveis e seus preços
def ver_menu():
        print(f"| {'ID':<4} | {'Produto':<25} | {'Preço':<13} |")
        print("-"*48)
        for id, info in estoque.items():
            print(f"| {id:<4} | {info['nome']:<25} | R${info['preco']:<12.2f}|")
        print("-"*48)
    
#função que adiciona ou remove itens em um carrinho de compras que reune todos os itens que o usuario selecionar a uma lista 
def alterar_carrinho(carrinho):
        
        print("digite (1) caso deseje adicionar itens ao carrinho, (2) para remover itens e (3) para voltar ao menu:")
        try:
            entrada = []
            fluxo = int(input(">> "))

            if fluxo == 1:
                try:
                    print("Digite o ID do item que voçe deseja comprar: ")
                    entrada = int(input(">> "))

                    if entrada in estoque:
                        carrinho.append(entrada)
                        print(f"O item '{estoque[entrada]['nome']}' no valor de R${estoque[entrada]['preco']:.2f} foi adicionado ao carrinho")
                except:
                    print("Item inexistente, nenhum item foi adicionado ao carrinho")
                    return 
            if fluxo == 2:
                print("Digite o ID do item que voçe deseja remover: ")
                try:
                    entrada = int(input(">> "))

                    if entrada == "": #or entrada not in estoque() or entrada not in carrinho:
                        print("Nenhum item foi removido do carrinho")
                        print("-"*48)
                    elif entrada not in carrinho:
                        print('O item digitado não esta no carrinho, caso queira ver seu carrinho volte volte ao menu')
                    
                    carrinho.remove(entrada) 
                    print(f"Item de indice {entrada} removido com sucesso do seu carrinho")
                except:
                    print("Item inexistente, nenhum item foi removido ao carrinho")
                    return 
            if fluxo == 3:
                print("Voltando ao menu...")
                print("-"*48) 

        except (ValueError, TypeError):
            print("Essa função do programa so aceita numeros como resposta.")
            return 
        except Exception as erro:
            print(f"Um erro inesperado aconteceu: {erro}")
            return 
        else:
            print("-"*48)
            return carrinho

    #Função para a visualização dos itens no carrinho, mostra indice do item, nome, preço e ao final soma o valor dos itens e mostra o valor total
def ver_carrinho(carrinho):
        print("-"*48)
        if len(carrinho) != 0:
            total=0
            print(f'{"CARRINHO":^50}')
            print(f"| {'ID':<3} | {'Produto':<25} | {'Preço':<13} |")
            print("-"*48)
            for item in carrinho:
                print(f"| {item} | {estoque[item]['nome']:<25} | R${estoque[item]['preco']:<12.2f}|")
                total = total + estoque[item]['preco']
            print(f"Valor total: R${total:.2f}")

        else:
            print("Nenhum item adicionado ao carrinho ainda!")
            return 
        return carrinho

#Menu onde deve começar a aplicação, onde aparecera as opções do user e como acessalas
def menu_principal():
    carrinho = []
    while True:
        print(f'{"Menu Principal":^50}')
        print('-'* 48)
        print("Opções:")
        print("(1) Ver Menu de Itens  (2) Adicionar/Remover Itens ao Carrinho   (3) Ver Carrinho e Confirmar Compra   (4)Sair")
        
        fluxo = int(input(">> "))

        if fluxo == 1:
                print("-"*48)
                ver_menu()
        elif fluxo == 2:
                print("-"*48)
                alterar_carrinho(carrinho)
        elif fluxo == 3:
                print("-"*48)
                ver_carrinho(carrinho)
        elif fluxo == 4:
                print("Saindo...")
                break
        else:
                print("Escolha uma opção valida para continuar")
                print("-"*48)
                continue    
                   
menu_principal()         
#TODO fazer confirmação do pedido, podendo ser uma função nova, ou uma extensão da funçao de ver carrinho, ou um pouco dos dois, ela so podera ser acessada caso haja algum item no carrinho, ela funcionara dando opções de pagamento e desconto a cada uma, ao confirmar pagamento o carrinho deve ser limpo para o proximo uso   

"""Exemplo de fluxo para a V3:
Início: O sistema exibe o menu de produtos com códigos e preços.
Loop de Compra: O usuário digita o código (ex: 1).
Validação: O sistema verifica se o código existe no dicionário.
Carrinho: O sistema adiciona o indice do produto em uma lista chamada carrinho.
TODO Fechamento: O usuário digita 0 ou fim. O sistema soma tudo, aplica os descontos que você já criou e pede a confirmação.
Itens a adicionar:
1. menu de compra, função que quando chamada mostrara todos os peodutos e seus preços, usar um laço for.
TODO 2. tenatar add um historico de compras, onde ao confirmar o pedido o python abre um arquivo.txt e escreve o produto, o preço, a quantidade, o horario e data
TODO 3. adicionar um sistema de estoque, quantidade inicial de itens que ao serem comprados alteram o valor do estoque e implementar a visualização em outras funções, como as citadas acima
TODO 4. adicionar como se fosse uma nota fiscal apos a confirmaçao da compra"""