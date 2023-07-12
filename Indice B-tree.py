import sqlite3

# Função para criar a tabela e o índice B-Tree
def criar_tabela_indice():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela (
            chave TEXT PRIMARY KEY,
            valor TEXT
        )
    ''')

    # Criação do índice B-Tree
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS indice_btree ON tabela (chave)
    ''')

    conexao.commit()
    conexao.close()

# Função para inserir um par chave-valor na tabela
def inserir_na_tabela(chave, valor):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Insere o par chave-valor na tabela
    cursor.execute('''
        INSERT INTO tabela (chave, valor)
        VALUES (?, ?)
    ''', (chave, valor))

    conexao.commit()
    conexao.close()

# Função para buscar um valor na tabela usando o índice B-Tree
def buscar_na_tabela(chave):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Executa a consulta usando o índice B-Tree
    cursor.execute('''
        SELECT valor FROM tabela WHERE chave = ?
    ''', (chave,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is not None:
        return resultado[0]
    else:
        return None

# Função para exibir todos os elementos da tabela
def mostrar_elementos_tabela():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Seleciona todos os elementos da tabela
    cursor.execute('''
        SELECT chave, valor FROM tabela
    ''')

    elementos = cursor.fetchall()

    if elementos:
        print("===== ELEMENTOS NA TABELA =====")
        for elemento in elementos:
            print(f"Chave: {elemento[0]}, Valor: {elemento[1]}")
    else:
        print("A tabela está vazia.")

    conexao.close()

# Função para exibir o menu e realizar as operações
def exibir_menu():
    while True:
        print("===== MENU =====")
        print("1. Inserir elemento na tabela")
        print("2. Buscar elemento na tabela")
        print("3. Mostrar todos os elementos da tabela")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            chave = input("Digite a chave: ")
            valor = input("Digite o valor: ")
            inserir_na_tabela(chave, valor)
            print("Elemento inserido na tabela.")
        elif escolha == "2":
            chave = input("Digite a chave a ser pesquisada: ")
            valor = buscar_na_tabela(chave)
            if valor is not None:
                print("Valor encontrado: ", valor)
            else:
                print("Chave não encontrada na tabela.")
        elif escolha == "3":
            mostrar_elementos_tabela()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
criar_tabela_indice()
exibir_menu()
