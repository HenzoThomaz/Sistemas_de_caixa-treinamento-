from conexao_bd import criar_conexao


#Função que visualiza itens em cadastrados em estoque, mais detalhes la em baixo
def ver_itens():
    try:
        conectar = criar_conexao()
        if not conectar:
            print("Não foi possivel conectar no banco de dados")
            return
        cursor = conectar.cursor(dictionary=True)

        comando = "SELECT * FROM estoque"
        cursor.execute(comando)
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto cadastrado ainda")
            print('-'*110)
            print()
            return

        print(f'{"--- Produtos Cadastrados ---":^110}')
        print('-'*110)
        print(f"| {'ID':<4} | {'Produto':<25} | {'Preço':<13} | {'Estoque':<4} |")
        print("-"*55)

        for produto in produtos:
            id = produto['id_produto']
            nome = produto['nome_produto']
            preco = produto['preco_produto']
            quantidade = produto['quantidade_estoque']
            print(f"| {id:<4} | {nome:<25} | R${preco:^10.2f} | {quantidade:^7} |")
        print("-"*110)
        print()
        print()
        return

    except Exception as erro:
          print(erro)
          return 
    
    finally:
        cursor.close()
        conectar.close()
          
#Função de cadastrar novo item ao sistema, adiciona estoque inicial e informações sobre o produto, parte do fluxo 2  
def cadastro_itens():
    try:
        conectar = criar_conexao()
        if not conectar:
            print("Não foi possivel conectar no banco de dados")
            return
        cursor = conectar.cursor()

        #parte da função que adiciona novo produto
        print(f"{'Cadatro de Produtos':^110}")
        print('-'* 110)
        print("O sistema adiciona um item por vez, sera pedido separadamente as informações sobre o produto a seguir")

        #loop para continuar cadastrando produtos
        while True:
            try:
                print("Nome do Produto")
                nome = input(">> ")
                print("Valor do Produto (Ex:10,00)")
                valor = input(">> ")
                print("Quantidade em estoque (Ex: 50) ")
                estoque = int(input(">> "))
                            
                #tratamento de valor
                valor = valor.replace(",",".")
                valor = float(valor)
                            
                #parte de inserir itens no banco
                try:
                    comando = "INSERT INTO estoque (nome_produto, preco_produto, quantidade_estoque) VALUES (%s, %s, %s)"
                    valores = (nome, valor, estoque)
                    cursor.execute(comando, valores)
                    conectar.commit()

                except Exception as erro:
                    print(f"Aconteceu um erro ao enviar informações ao banco: {erro}")
                    return

                print(f"O produto {nome} foi cadastrado com sucesso!")
                print("Deseja continuar cadastrando produtos? (S/N)")
                fluxo = input(">> ").lower()
                if fluxo == "s":
                    print("-"*110)
                    print("Insira as informações do novo produto:")
                    continue
                else:
                    print("Voltando...")
                    return

            except:
                print("Voçe inseriu algum dado em um formato não suportado")
                continue

    except Exception as erro:
        print(erro)
        return
    
    finally:
        cursor.close()
        conectar.close()

#Função de remover item do sistema, remove todas as informações do item, parte do fluxo 2
def remover_cadastro():
    try:
        conectar = criar_conexao()
        if not conectar:
            print("Problemas ao conectar ao banco de dados")
            return
        cursor = conectar.cursor(dictionary=True)

        #parte da função que descreve o que o usuario deve fazer 
        print(f"{'Remover Produtos':^110}")
        print('-'* 110)
        print("O sistema remove um item por vez, sera necessario somente o id  do produto, apos a confirmação o item sera excluido do sistema, use com cautela!")

        #loop para continuar excluindo itens caso queira
        while True:
            print("Id do produto a ser excluido, ou 's' para voltar")
            id_delete = input(">> ").lower()
            #escolha de opções e tratamento da entrada 
            try:
                if id_delete == "s":
                    print("Voltando...")
                    return
                
                id_delete = int(id_delete)
                id_delete = (id_delete,)

                #verifica se o produto realmente existe no sistema
                try:
                    cursor.execute("SELECT nome_produto FROM estoque WHERE id_produto = %s;", id_delete)
                    produto = cursor.fetchone()
                    nome = produto['nome_produto']
                except Exception as erro:
                    print(f"Erro ao conectar com o banco de dados para conferir produto: {erro}")

                if not produto:
                    print("O ID digitado não esta cadastrado no estoque")
                    print()
                    continue
                
                #sse existe, confirma se quer excluir 
                print(f"Deseja mesmo excluir o produto {nome}? 'S' para continuar")
                fluxo1 = input(">> ").lower()
                if fluxo1 != 's':
                    print("Exclusão cancelada")
                    return
                
                #comando de exclusao
                try:
                    comando = "DELETE FROM estoque WHERE id_produto = %s;"
                    cursor.execute(comando, id_delete)
                    conectar.commit()

                except Exception as erro:
                    print(f"Ocorreu um erro ao enviar as informações ao banco: {erro}")
                    return

                #deseja continuar DELETANDO PRODUTOS?   
                print(f"O produto {nome} foi excuido com sucesso!")
                print("Deseja excluir mais algum produto? (S/N)")
                fluxo = input(">> ").lower()
                if fluxo == "s":
                    continue
                else:
                    print("Voltando...")
                    break

#tratamento de erros e fechar o banco de dados
            except:
                print("Digite um ID valido")
                continue
    except Exception as erro:
        print(f"Aconteceu um erro inesperado: {erro}")
        return 
    
    finally:
        conectar.close()
        cursor.close()

def menu_principal():
    while True:
        print(f'{"Menu Principal do Funcionario":^110}')
        print('-'* 110)
        print("Opções:")
        print("(1) Ver Itens Cadastradoos e Estoque  (2) Cadastrar/Remover Itens  (3) Adicionar/Remover Estoque   (4)Sair")
        try:
            fluxo = int(input(">> "))
            if fluxo == 1:
                print("-"*110)
                ver_itens()

            elif fluxo == 2:
                print("-"*110)
                print(f'{"-- Cadastro e Exclusão de Produtos --":^110}')
                print('-'* 110)
                print("(1) Cadastrar Novo Produto  (2)Excluir Produto do Sistema  (3)Voltar")
                while True:
                    fluxo2 = input(">> ")
                    if fluxo2 == "1":
                        cadastro_itens()
                    elif fluxo2 == "2":
                        remover_cadastro() 
                    elif fluxo2 == "3":
                        print("Voltando..")
                        print()
                        break   
                    else:
                        print("escolha uma opção valida")
                        continue

            elif fluxo == 3:
                    print("-"*110)
                    #lugar de chamar a função
            elif fluxo == 4:
                    print("Saindo...")
                    break
        except:
                    print("Escolha uma opção valida para continuar")
                    print("-"*48)
                    continue    
                   
menu_principal() 




""""Função de ver itens, primeiro ela faz a conexão ao bd criando uma variavel pra chamar a função, e caso ela retorn true ela continua se n, volta ao loop inicial, definimos um cursor, que tera a função de executar os comandos no sql, ele esta com o dicionario ativo, fazendo ele retornar um dicionario, e nao uma lista com tuplas, que eh o padrão, definimos a variavel com o comando e depois a utilizamos, retornando a resposta que eh o dicionario em outra variavel, depois 'traduzimos' cada elemento ao python por meio do loop for, ja que ele retorna em dicionario onde o nome de cada  indice eh o nome da coluna e seu respectivo resultado, ele repete esse padrão para todas as colunas e linhas transformando em um dicionario """

"""toda vez que quiser chamar o banco em alguma função eu crio uma variavez que chame a função e caso ela seje true eu continuo meu codico, isso significa quee ela conectou ao banco, se der false eu retorno ao loop inicial por exxemplo

para manipular itens usando comandos sql(para aprendizado, ideal eh orm ou similares) eu defino uma nova variavel que contera -- (var de conexao).(var de cursor)(parentese vazio no final) -- ai para comandos, query eu uso o cursor e para comandos direto ao banco eu uso o de bd"""