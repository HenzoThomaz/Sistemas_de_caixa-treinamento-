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
#Criação das funções
def carrinho():
  pass






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