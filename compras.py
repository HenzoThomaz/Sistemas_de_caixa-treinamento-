print("---------Sistema de Compras---------")
while True:
    nome_produto = []
    valor_produto = []
    num_produtos = int(input("Quantos produtos voçe comprou? "))

    for produto in range(num_produtos):
        nome = input("Nome do produto: ")
        nome_produto.append(nome) 
        valor = float(input(f"Valor do(a) {nome}: "))
        valor_produto.append(valor)

    total = sum(valor_produto)
    maior_valor = max(valor_produto)
    indice_maior_valor = valor_produto.index(maior_valor)
    nome_produto_caro = nome_produto[indice_maior_valor]
    print("-"* 30)
    if total > 100:
        total_descontado = total * 0.85
        print(f"O valor total da sua compra eh de R${total:.2f}, por passar de R$100,00 voçe ganhou 15% de desconto, ficando R${total_descontado:.2f}!! E seu produto mais caro comprado eh {nome_produto_caro}, no valor de R${maior_valor:.2f}")
    else: 
        print(f"O valor total da sua compra eh de R${total:.2f} e seu produto mais caro comprado eh {nome_produto_caro}, no valor de R${maior_valor:.2f}")
    print("-"*30)


    continuar = input("Se quiser continuar no sistema de compras digite 'S', caso não queira digite qualquer tecla: ").lower()
    if continuar != "s":
        break

