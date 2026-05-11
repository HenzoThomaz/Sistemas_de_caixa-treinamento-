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

#TODO teste em toda essa função

#Função de pagamento, fornece diferentes opções de pagamento ao cliente e seus respectivos descontos, ao fazer a confirmação deve retornar ao menu com o carrinho zerado, como se fosse um novo cliente
def pagamento(total, carrinho):
    print("-"*110)
    print(f"O total de sua compra ficou em R${total:.2f}, escolha a opção de pagamento dentre as seguintes:")
    print("(1) Pix ou Dinheiro (15% off)   (2) Debito ou Credito a vista (10% off)   (3) Crédito parcelado max:15 (ate 5x sem juros e acima de 5x 10% de acrescimo) "
    "  (4) Cancelar pagamento")

    try:
        fluxo = int(input(">> ")) 
        
        if fluxo == 1:
            total_15 = total * 0.85
            print(f"O valor com o desconto de 15% fica em R${total_15:.2f}")

        if fluxo == 2:
            total_10 = total * 0.90
            print(f"O valor com o desconto de 10% fica em R${total_10:.2f}")

        if fluxo == 3:
            print("Insira quantas parcelas voçe deseja parcelar.")
            while True:
                parcelas = int(input(">> "))
                if parcelas >= 2 and parcelas <= 5:
                    total_par = total / parcelas
                    print(f"O valor de cada parcela sem juros ficou em R${total_par:.2f}")
                    break
                elif parcelas >= 6 and parcelas <= 15:
                    total_plus = total * 1.10
                    total_plus /= parcelas
                    print(f"O valor de cada parcela com juros de 10% ficou em R${total_plus:.2f}")
                    break
                else:
                    print("Escolha um numero valido de parcelas.")
                    continue
        
        if fluxo == 4:
            print("Pagamento cancelado pelo cliente.")
            return 
        
        while True:
            print("Deseja confirmar o pagamento? (S/N)")
            resposta = input().lower()
            if resposta == "s":
                print("Pagamento concluido!!")
                break
            elif resposta == "n":
                print("Pagamento cancelado pelo usuario.")
                return
            else:
                print("Escolha uma opção valida")
                continue

    except:
        print("Por que vc esta sempre tentando quebrar o codico???")
        return 
    else:
        total = 0
        carrinho.clear()
        print("Obrigado pela compra e volte sempre!!")
        print("-"*110)
        return carrinho

#função que chama um menu que mostrara os itens disponiveis e seus preços
def ver_menu():
        print(f"| {'ID':<4} | {'Produto':<25} | {'Preço':<13} |")
        print("-"*48)
        for id, info in estoque.items():
            print(f"| {id:<4} | {info['nome']:<25} | R${info['preco']:<12.2f}|")
        print("-"*48)
    
#função que adiciona ou remove itens em um carrinho de compras que reune todos os itens que o usuario selecionar a uma lista 
def alterar_carrinho(carrinho):
        
        print("digite (1) caso deseje adicionar itens ao carrinho  (2) para remover itens  (3) para voltar ao menu:")
        try:
            entrada = []
            fluxo = int(input(">> "))

            if fluxo == 1:
                try:
                    print("Digite o ID do item que voçe deseja comprar: ")
                    txt_usuario = input(">> ")
                    entrada = [int(id.strip()) for id in txt_usuario.split(",")]
                    #a linha acima foi a unica q peguei a ideia da IA, paia demaisi
                    for item in entrada:
                            carrinho.append(item)
                            print(f"O item '{estoque[item]['nome']}' no valor de R${estoque[item]['preco']:.2f} foi adicionado ao carrinho")
                except:
                    print("Item inexistente, nenhum item foi adicionado ao carrinho")
                    return 
            if fluxo == 2:
                print("Digite o ID do item que voçe deseja remover ou digite 0 para remover todos: ")
                try:
                    entrada = int(input(">> "))

                    if entrada == 0:
                        carrinho.clear()
                        print("Todos os itens foram removidos do carrinho")
                        return
                    elif entrada not in carrinho:
                        print('O item digitado não esta no carrinho, caso queira ver seu carrinho volte volte ao menu')
                    
                    carrinho.remove(entrada) 
                    print(f"Item {estoque[entrada]['nome']} foi removido com sucesso do seu carrinho")
                except:
                    print("Item inexistente, nenhum item foi removido ao carrinho")
                    return 
            if fluxo == 3:
                print("Voltando ao menu...")
                print("-"*110) 

        except (ValueError, TypeError):
            print("Essa função do programa so aceita numeros como resposta.")
            return 
        except Exception as erro:
            print(f"Um erro inesperado aconteceu: {erro}")
            return 
        else:
            print("-"*110)
            return carrinho

#Função para a visualização dos itens no carrinho, mostra indice do item, nome, preço e ao final soma o valor dos itens e mostra o valor total
def ver_carrinho(carrinho):
        fluxo_carrinho = 0
        if len(carrinho) != 0:
            total=0
            print(f'{"CARRINHO":^50}')
            print(f"| {'ID':<3} | {'Produto':<25} | {'Preço':<13} |")
            print("-"*51)
            for item in carrinho:
                print(f"| {item}  | {estoque[item]['nome']:<25} | R${estoque[item]['preco']:<12.2f}|")
                total = total + estoque[item]['preco']
            print(f"Valor total: R${total:.2f}")
            print('-'*51)
            print("Digite (1) para confirmar seu pedido e ir a sessão de pagamento. Caso não, aperte qualquer tecla.")
            try:
                fluxo_carrinho = int(input(">> "))
                if fluxo_carrinho == 1:
                     return total and carrinho and pagamento(total, carrinho)
            except:
                return carrinho
        else:
            print("Nenhum item adicionado ao carrinho ainda!")
            print('-'*110)
            return 
        return carrinho 

#Menu onde deve começar a aplicação, onde aparecera as opções do user e como acessalas
def menu_principal():
    carrinho = []
    while True:
        print(f'{"Menu Principal":^110}')
        print('-'* 110)
        print("Opções:")
        print("(1) Ver Menu de Itens  (2) Adicionar/Remover Itens ao Carrinho   (3) Ver Carrinho e Confirmar Compra   (4)Sair")
        try:
            fluxo = int(input(">> "))
            if fluxo == 1:
                    print("-"*110)
                    ver_menu()
            elif fluxo == 2:
                    print("-"*110)
                    alterar_carrinho(carrinho)
            elif fluxo == 3:
                    print("-"*110)
                    ver_carrinho(carrinho)
            elif fluxo == 4:
                    print("Saindo...")
                    break
        except:
                    print("Escolha uma opção valida para continuar")
                    print("-"*48)
                    continue    
                   
menu_principal()         

"""Exemplo de fluxo para a V3:
Início: O sistema exibe o menu de produtos com códigos e preços.
Loop de Compra: O usuário digita o código (ex: 1).
Validação: O sistema verifica se o código existe no dicionário.
Carrinho: O sistema adiciona o indice do produto em uma lista chamada carrinho.
Fechamento: O usuário digita 0 ou fim. O sistema soma tudo, aplica os descontos que você já criou e pede a confirmação.

Itens a adicionar:
TODO 1. sistema de gerenciamento de estoque em outro arquivo python linkado a esse, que sera a pagina "vendedor", que fara todo controle de estoque e podemos mudar ate mesmo a variavel de estoque para la ou transformala em um arquivo proprio
TODO 2. tenatar add um historico de compras, onde ao confirmar o pedido o python abre um arquivo.txt e escreve o produto, o preço, a quantidade, o horario e data
TODO 3. adicionar como se fosse uma nota fiscal apos a confirmaçao da compra"""