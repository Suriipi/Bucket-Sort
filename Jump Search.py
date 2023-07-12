import math
import sqlite3

# Função para criar a tabela
def criar_tabela():
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

# Função para realizar uma busca pelo valor na tabela usando o Jump Search
def buscar_na_tabela(valor):
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Realiza a busca pelos blocos usando Jump Search
    total_elementos = cursor.execute('SELECT COUNT(*) FROM tabela').fetchone()[0]
    tamanho_bloco = int(math.sqrt(total_elementos))

    bloco_inicial = 0
    bloco_final = tamanho_bloco

    while bloco_final < total_elementos and valor >= cursor.execute('SELECT valor FROM tabela LIMIT 1 OFFSET ?', (bloco_final,)).fetchone()[0]:
        bloco_inicial = bloco_final
        bloco_final += tamanho_bloco

    # Realiza a busca linear dentro do bloco encontrado
    cursor.execute('SELECT chave, valor FROM tabela WHERE valor = ? AND chave >= ? AND chave <= ?',
                   (valor, bloco_inicial, bloco_final))
    resultado = cursor.fetchall()

    conexao.close()

    if resultado:
        return resultado
    else:
        return None

# Função para exibir todos os elementos da tabela
def mostrar_elementos_tabela():
    conexao = sqlite3.connect('base_de_dados.db')
    cursor = conexao.cursor()

    # Seleciona todos os elementos da tabela
    cursor.execute('SELECT chave, valor FROM tabela')
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
            chave = int(input("Digite a chave (inteiro): "))
            valor = input("Digite o valor: ")
            inserir_na_tabela(chave, valor)
            print("Elemento inserido na tabela.")
        elif escolha == "2":
            valor = input("Digite o valor a ser pesquisado: ")
            resultado = buscar_na_tabela(valor)
            if resultado:
                print("Resultado encontrado:")
                for r in resultado:
                    print(f"Chave: {r[0]}, Valor: {r[1]}")
            else:
                print("Valor não encontrado na tabela.")
        elif escolha == "3":
            mostrar_elementos_tabela()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
criar_tabela()
exibir_menu()
