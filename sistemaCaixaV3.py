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
carrinho = []
on = True
#Criação das funções

#função que chama um menu que mostrara os itens disponiveis e seus preços
def ver_menu():
        print(f"| {'ID':<4} | {'Produto':<25} | {'Preço':<13} |")
        print("-"*48)
        for id, info in estoque.items():
            print(f"| {id:<4} | {info['nome']:<25} | R${info['preco']:<12.2f}|")
        print("-"*48)

        return
    
#TODO por enquanto ela so aceita um item por vez, podemos mecher 
#função que adiciona ou remove itens em um carrinho de compras que reune todos os itens que o usuario selecionar a uma lista 
def alterar_carrinho(carrinho):
        
        print("digite (1) caso deseje adicionar itens ao carrinho, (2) para remover itens e (3) para voltar ao menu:")
        try:
            entrada = []
            carrinho = []
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
                    return carrinho
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
                    return carrinho
            if fluxo == 3:
                print("Voltando ao menu...")
                print("-"*48)
                return menu_principal

        except (ValueError, TypeError):
            print("Essa função do programa so aceita numeros como resposta.")
            return carrinho
        except Exception as erro:
            print(f"Um erro inesperado aconteceu: {erro}")
            return carrinho
        else:
            print("-"*48)
            return carrinho

    #TODO tentar fazer a função de ver carrinho funcionar, pq n sei linkar variaveis em outras funções, estou usando como parametro mas n sei como funciona e conseguir fazer que para cara item no carrinho ele puxe e escreva seu nome e preço numa tabela e some os valores ao final

"""carrinho = alterar_carrinho(carrinho)
    print(carrinho)"""

def ver_carrinho(carrinho):
        print("-"*48)
        if len(carrinho) != 0:
            total=0
            print(f'{"CARRINHO":^50}')
            print(f"| {'Produto':<25} | {'Preço':<13} |")
            print("-"*48)
            for item in carrinho:
                print(f"| {estoque[item]['nome']:<25} | R${estoque[item]['preco']:<12.2f}|")
                total = total + estoque[item]['preco']
            print(f"Valor total: R${total:.2f}")

        else:
            print("Nenhum item adicionado ao carrinho ainda!")
            return 
        return carrinho

#TODO arrumar esse loop, e dar um jeito de fazer a função de menu funcionar
#Menu onde deve começar a aplicação, onde aparecera as opções do user e como acessalas
while on :
    def menu_principal(on):
        print(f'{"Menu Principal":^50}')
        print('-'* 48)
        print("Opções:")
        print("(1) Ver Menu   (2) Alterar Carrinho   (3) Ver Carrinho   (4)Sair")
        try:
            fluxo == input(">>")
            fluxo = int()

            if fluxo == 1:
                return ver_menu()
            if fluxo == 2:
                return alterar_carrinho(carrinho)
            if fluxo == 3:
                return ver_carrinho(carrinho)
            if fluxo == 4:
                print("Saindo...")
                on == False
        except:
            print("Escolha uma opção valida para continuar")
            return
            
    menu_principal(on)
"""Exemplo de fluxo para a V3:
Início: O sistema exibe o menu de produtos com códigos e preços.
Loop de Compra: O usuário digita o código (ex: 1).
Validação: O sistema verifica se o código existe no dicionário.
Carrinho: O sistema adiciona o dicionário do produto em uma lista chamada carrinho.
Fechamento: O usuário digita 0 ou fim. O sistema soma tudo, aplica os descontos que você já criou e pede a confirmação.
Itens a adicionar:
1. menu de compra, função que quando chamada mostrara todos os peodutos e seus preços, usar um laço for.
2. tenatar add um historico de compras, onde ao confirmar o pedido o python abre um arquivo.txt e escreve o produto, o preço, a quantidade, o horario e data
3. adicionar um sistema de estoque, quantidade inicial de itens que ao serem comprados alteram o valor do estoque e implementar a visualização em outras funções, como as citadas acima
4. adicionar como se fosse uma nota fiscal apos a confirmaçao da compra"""