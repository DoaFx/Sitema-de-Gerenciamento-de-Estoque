from datetime import datetime

#Estrutura de Dados
categorias = {}
produtos = {}
movimentacoes = []

#Função CADASTRO CATEGORIA
def cadastrar_categoria(nome):
    if nome not in categorias:
        categorias[nome] = []
        print (f"Categoria '{nome}' cadastrada\n")
    else:
        print(f"Categoria '{nome} já existe\n")

#Função CADASTRO PRODUTO
def cadastrar_produto (id_produto, nome, categoria, preco, quantidade=0):
    if categoria not in categorias:
        print(f"Categoria '{categoria}' não existe\n")
        return
    else:    
        produtos[id_produto] = {'nome': nome, 'categoria': categoria, 'preco': preco, 'quantidade': quantidade}
        categorias[categoria].append(id_produto)
        print(f"Produto '{nome}' cadastrado na categoria '{categoria}'\n")
        return

#Função CONSULTAR PRODUTO
def consultar_produto (id_produto):
    if id_produto not in produtos:
        print(f"Produto de ID:'{id_produto}' não encontrado")
        return
    else:
        p = produtos[id_produto]
        print(f"Produto: {p['nome']}, Categoria: {p['categoria']}, Preço: {p['preco']}, Quantidade: {p['quantidade']}\n")
        return

#Função MOVIMENTAR PRODUTO
def movimentar_produto(id_produto, quantidade, tipo):
    if id_produto not in produtos:
        print(f"Produto ID:'{id_produto}' não encontrado\n")
        return
    if tipo == 'entrada':
        produtos[id_produto]['quantidade'] += quantidade
    elif tipo == 'saida':
        if produtos[id_produto]['quantidade'] >= quantidade:
            produtos[id_produto]['quantidade']-= quantidade
        else:
            print("Quantidade insuficiente no estoque\n")
            return
    movimentacoes.append({'tipo': tipo, 'produto': id_produto, 'quantidade': quantidade, 'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S')})
    print(f"{tipo.capitalize()} de {quantidade} unidades do produto '{produtos[id_produto]['nome']}' registrada.\n")
    

#Função GERAR RELATÓRIO DE PRODUTOS
def gerar_relatorio_produtos():
    print("Relatório de produtos em Estoque: ")
    for id_produto, p in produtos.items():
         print(f"ID: {id_produto}, Nome: {p['nome']}, Quantidade: {p['quantidade']}, Preço: {p['preco']}\n")
   
#Função CONSULTAR MOVIMENTAÇÕES
def consultar_historico_movimentacoes():
    print("Histórico de Movimentações: ")
    for mov in movimentacoes:
        p = produtos[mov['produto']]
        print(f"Tipo: {mov['tipo']}, Produto: {p['nome']}, Quantidade: {mov['quantidade']}, Data: {mov['data']}\n")

#Exemplo de uso para cadastrar categoria
cadastrar_categoria("Mouse")

#Exemplo de uso para cadastrar produto 
cadastrar_produto(1, "Redragon Cobra", "Mouse", 5, 150)

#Exemplo de uso para consultar produto
consultar_produto(1)

#Exemplo de uso para movimentar produto
movimentar_produto(1, 5, 'saida')

#Exemplo de uso para gerar relatorio de produtos
gerar_relatorio_produtos()

#Exemplo de uso para consultar histórico de movimentações
consultar_historico_movimentacoes()


