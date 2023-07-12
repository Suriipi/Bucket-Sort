import sqlite3

# Classe para representar um nó na árvore BST
class Node:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Classe para representar a árvore BST
class BST:
    def __init__(self):
        self.raiz = None

    # Método para inserir um nó na árvore
    def inserir(self, chave, valor):
        if self.raiz is None:
            self.raiz = Node(chave, valor)
        else:
            self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no, chave, valor):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = Node(chave, valor)
            else:
                self._inserir_recursivo(no.esquerda, chave, valor)
        else:
            if no.direita is None:
                no.direita = Node(chave, valor)
            else:
                self._inserir_recursivo(no.direita, chave, valor)

    # Método para buscar um valor na árvore
    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no.valor
        if chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        return self._buscar_recursivo(no.direita, chave)

    # Método para exibir todos os elementos da árvore em ordem
    def mostrar_elementos(self):
        if self.raiz is not None:
            self._mostrar_recursivo(self.raiz)

    def _mostrar_recursivo(self, no):
        if no is not None:
            self._mostrar_recursivo(no.esquerda)
            print(f"Chave: {no.chave}, Valor: {no.valor}")
            self._mostrar_recursivo(no.direita)

# Função para criar a tabela e a árvore BST
def criar_tabela_arvore():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela (
            chave INTEGER PRIMARY KEY,
            valor TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

# Função para inserir um par chave-valor na tabela e na árvore BST
def inserir_na_tabela_arvore(chave, valor):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Insere o par chave-valor na tabela
    cursor.execute('''
        INSERT INTO tabela (chave, valor)
        VALUES (?, ?)
    ''', (chave, valor))

    conexao.commit()
    conexao.close()

    # Insere o par chave-valor na árvore BST
    arvore.inserir(chave, valor)

# Função para buscar um valor na tabela e na árvore BST
def buscar_na_tabela_arvore(chave):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Executa a consulta na tabela
    cursor.execute('''
        SELECT valor FROM tabela WHERE chave = ?
    ''', (chave,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is not None:
        return resultado[0]
    else:
        return None

# Função para exibir o menu e realizar as operações
def exibir_menu():
    while True:
        print("===== MENU =====")
        print("1. Inserir elemento na tabela e na árvore")
        print("2. Buscar elemento na tabela e na árvore")
        print("3. Mostrar todos os elementos da árvore")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            chave = int(input("Digite a chave (inteiro): "))
            valor = input("Digite o valor: ")
            inserir_na_tabela_arvore(chave, valor)
            print("Elemento inserido na tabela e na árvore.")
        elif escolha == "2":
            chave = int(input("Digite a chave a ser pesquisada (inteiro): "))
            valor = buscar_na_tabela_arvore(chave)
            if valor is not None:
                print("Valor encontrado: ", valor)
            else:
                print("Chave não encontrada na tabela e na árvore.")
        elif escolha == "3":
            arvore.mostrar_elementos()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
arvore = BST()
criar_tabela_arvore()
exibir_menu()
