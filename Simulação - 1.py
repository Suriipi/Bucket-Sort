class Produto:
    def __init__(self, codigo, nome, unidade_medida, quantidade_estoque, preco_compra, preco_venda):
        self.codigo = codigo
        self.nome = nome
        self.unidade_medida = unidade_medida
        self.quantidade_estoque = quantidade_estoque
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda

class Cooperativa:
    def __init__(self):
        self.produtos = []

    def cadastrar(self):
        quantidade = int(input("Digite a quantidade de produtos a serem cadastrados: "))
        for i in range(quantidade):
            codigo = int(input("Digite o código do produto: "))
            nome = input("Digite o nome do produto: ")
            unidade_medida = input("Digite a unidade de medida do produto: ")
            quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))
            preco_compra = float(input("Digite o preço de compra do produto: "))
            preco_venda = float(input("Digite o preço de venda do produto: "))
            produto = Produto(codigo, nome, unidade_medida, quantidade_estoque, preco_compra, preco_venda)
            self.produtos.append(produto)
        print("Produtos cadastrados com sucesso!")

    def pesquisar(self):
        codigo = int(input("Digite o código do produto: "))
        for produto in self.produtos:
            if produto.codigo == codigo:
                print("Código: ", produto.codigo)
                print("Nome: ", produto.nome)
                print("Unidade de Medida: ", produto.unidade_medida)
                print("Quantidade em Estoque: ", produto.quantidade_estoque)
                print("Preço de Compra: ", produto.preco_compra)
                print("Preço de Venda: ", produto.preco_venda)
                break
        else:
            print("Produto não encontrado!")

    def excluir(self):
        codigo = int(input("Digite o código do produto a ser excluído: "))
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print("Produto excluído com sucesso!")
                break
        else:
            print("Produto não encontrado!")

    def listar(self):
        for produto in self.produtos:
            print("Código: ", produto.codigo)
            print("Nome: ", produto.nome)
            print("Unidade de Medida: ", produto.unidade_medida)
            print("Quantidade em Estoque: ", produto.quantidade_estoque)
            print("Preço de Compra: ", produto.preco_compra)
            print("Preço de Venda: ", produto.preco_venda)

    def quicksort(self, lista, inicio, fim):
        if inicio < fim:
            pivo = self.partition(lista, inicio, fim)
            self.quicksort(lista, inicio, pivo-1)
            self.quicksort(lista, pivo+1, fim)

    def partition(self, lista, inicio, fim):
        pivo = lista[fim].quantidade_estoque
        i = inicio - 1
        for j in range(inicio, fim):
            if lista[j].quantidade_estoque < pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i+1], lista[fim] = lista[fim], lista[i+1]
        return i+1

    def ordenar_estoque(self):
        self.quicksort(self.produtos, 0, len(self.produtos)-1)
        print("Produtos ordenados com sucesso!")

cooperativa = Cooperativa()

while True:
    print("\n========= MENU =========")
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Ordenar Estoque")
    print("9 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cooperativa.cadastrar()
    elif opcao == 2:
        cooperativa.pesquisar()
    elif opcao == 3:
        cooperativa.excluir()
    elif opcao == 4:
        cooperativa.listar()
    elif opcao == 5:
        cooperativa.ordenar_estoque()
    elif opcao == 9:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        
        




