#dados
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
fluxo = int()

#Criação das funções

#Menu onde deve começar a aplicação, onde aparecera as opções do user e como acessalas
def menu_principal():
    print("Menu Principal")

    if fluxo == 1:
       return ver_menu()
    
#função que chama um menu que mostrara os itens disponiveis e seus preços
def ver_menu():
  print(f"| {'ID':<4} | {'Produto':<25} | {'Preço':<13} |")
  print("-"*48)
  for id, info in estoque.items():
    print(f"| {id:<4} | {info['nome']:<25} | R${info['preco']:<12.2f}|")
  print("-"*48)

  return menu_principal()

#TODO fazer o try except ao invez de variaveis e if else paia pra caramba 
#função que adiciona ou remove itens em um carrinho de compras que reune todos os itens que o usuario selecionar a uma lista 
def item_carrinho():
    
    print("digite (1) caso deseje adicionar itens ao carrinho, (2) para remover itens e (3) para voltar ao menu:")
    fluxo = int(input(">> "))
    entrada = []

    if fluxo == 1:
        print("Digite o ID do item que voçe deseja comprar: ")
        entrada = input(">> ")
        if entrada == "" or entrada not in estoque.len() or entrada not in carrinho:
            print("Nenhum item foi adicionado ao carrinho")
            print("-"*48)
            return menu_principal()
        carrinho = []
        carrinho.append(entrada)

    if fluxo == 2:
        print("Digite o ID do item que voçe deseja remover: ")
        entrada = input(">> ")
        if entrada == "" or entrada not in estoque() or entrada not in carrinho:
            print("Nenhum item foi removido ao carrinho")
            print("-"*48)
            return menu_principal()
        carrinho=[]
        carrinho.remove(entrada) 

    else:
       print("Voltando ao menu principal")
       return menu_principal()
    
    print("-"*48)
    return carrinho

carrinho = item_carrinho()

def ver_carrinho():
   pass

ver_menu()
#variavel global de itens no carrinho




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