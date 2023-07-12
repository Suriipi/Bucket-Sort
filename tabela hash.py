import hashlib
import sqlite3

# Função para criar a tabela hash
def criar_tabela_hash():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Criação da tabela hash com dois campos: chave (hash) e valor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela_hash (
            chave TEXT PRIMARY KEY,
            valor TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

# Função para inserir um par chave-valor na tabela hash
def inserir_na_tabela_hash(chave, valor):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Calcula o hash da chave usando o algoritmo SHA-256
    hash_chave = hashlib.sha256(chave.encode()).hexdigest()

    # Insere o par chave-valor na tabela hash
    cursor.execute('''
        INSERT INTO tabela_hash (chave, valor)
        VALUES (?, ?)
    ''', (hash_chave, valor))

    conexao.commit()
    conexao.close()

# Função para buscar um valor na tabela hash
def buscar_na_tabela_hash(chave):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Calcula o hash da chave usando o algoritmo SHA-256
    hash_chave = hashlib.sha256(chave.encode()).hexdigest()

    # Busca o valor correspondente à chave na tabela hash
    cursor.execute('''
        SELECT valor FROM tabela_hash WHERE chave = ?
    ''', (hash_chave,))

    resultado = cursor.fetchone()

    conexao.close()

    if resultado is not None:
        return resultado[0]
    else:
        return None

# Função para exibir todos os elementos da tabela hash
def mostrar_elementos_tabela_hash():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Seleciona todos os elementos da tabela hash
    cursor.execute('''
        SELECT chave, valor FROM tabela_hash
    ''')

    elementos = cursor.fetchall()

    if elementos:
        print("===== ELEMENTOS NA TABELA HASH =====")
        for elemento in elementos:
            print(f"Chave: {elemento[0]}, Valor: {elemento[1]}")
    else:
        print("A tabela hash está vazia.")

    conexao.close()

# Função para exibir o menu e realizar as operações
def exibir_menu():
    while True:
        print("===== MENU =====")
        print("1. Inserir elemento na tabela hash")
        print("2. Buscar elemento na tabela hash")
        print("3. Mostrar todos os elementos da tabela hash")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            chave = input("Digite a chave: ")
            valor = input("Digite o valor: ")
            inserir_na_tabela_hash(chave, valor)
            print("Elemento inserido na tabela hash.")
        elif escolha == "2":
            chave = input("Digite a chave a ser pesquisada: ")
            valor = buscar_na_tabela_hash(chave)
            if valor is not None:
                print("Valor encontrado: ", valor)
            else:
                print("Chave não encontrada na tabela hash.")
        elif escolha == "3":
            mostrar_elementos_tabela_hash()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
criar_tabela_hash()
exibir_menu()


