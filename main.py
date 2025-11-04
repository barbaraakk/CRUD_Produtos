import sqlite3

def executar_script_sql(conn):
    try:
        cursor = conn.cursor()

        with open('db.sql', 'r', encoding='utf-8') as sql_file:
            sql_script = sql_file.read()
            cursor.executescript(sql_script)
            print("Script db.sql executado")

        conn.commit()
    except FileNotFoundError:
        print("Arquivo db.sql não encontrado.")
    except sqlite3.Error as error:
        print("Erro ao executar script SQL:", error)


def adicionar_produto(conn):
    cursor = conn.cursor()

    add = input("Deseja adicionar um produto? (sim/não)").strip().lower()

    while add == "sim":
        p_nome = input("Digite o nome do produto a ser cadastrado: ").strip()
        if not p_nome:
            print("O nome do produto é obrigatório.")
            continue

        try:
            p_preco = float(input("Digite o preço do produto: "))
            if p_preco < 0:
                print("O preço não pode ser negativo.")
                continue
        except ValueError:
            print("Digite um valor numérico válido para o preço.")
            continue

        try:
            p_quantidade = int(input("Digite a quantidade do produto: "))
            if p_quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
        except ValueError:
            print("Digite um número inteiro válido para a quantidade.")
            continue

        p_descricao = input("Descrição (opcional): ").strip() or None


        while True:
            p_data = input("Digite a data de validade. Use o formato yyyy-mm-dd (ex: 2025-11-04): ").strip()
            partes = p_data.split("-")
            if len(partes) == 3 and all(p.isdigit() for p in partes) and len(partes[0]) == 4 and len(partes[1]) == 2 and len(partes[2]) == 2:
                break
            print("Formato inválido. Use o formato yyyy-mm-dd (ex: 2025-11-04).")

        cursor.execute("""INSERT INTO produtos (nome, preco, quantidade, descricao, data_validade) VALUES (?,?,?,?,?)""", (p_nome, p_preco, p_quantidade, p_descricao, p_data))

        conn.commit()
        print("Produto inserido com sucesso.")
        add = input("Deseja adicionar mais um produto? (sim/não): ").strip().lower()
    else:
        print("Nenhum produto foi adicionado.")


def exibir_dados(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos;")
    dados = cursor.fetchall()

    if not dados:
        print("Nenhum produto cadastrado.")
    else:
        print("\nID  | Nome                     | Preço (R$) | Qtd  | Descrição           | Validade")
        print("-" * 90)
        for id, nome, preco, quantidade, descricao, data_validade in dados:
            descricao = descricao or ""
            print(f"{id:<3} | {nome:<24} | {preco:<10.2f} | {quantidade:<4} | {descricao:<20} | {data_validade}")
            print("-" * 90)

def buscar_por_id(conn):
    cursor = conn.cursor()
    buscar_por_id = input("Digite o ID do produto que deseja buscar: ").strip()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (buscar_por_id,))
    produto = cursor.fetchone()

    if produto:
        id, nome, preco, quantidade, descricao, data_validade = produto
        descricao = descricao or ""
        print("\nID  | Nome                     | Preço (R$) | Qtd  | Descrição           | Validade")
        print("-" * 90)
        print(f"{id:<3} | {nome:<24} | {preco:<10.2f} | {quantidade:<4} | {descricao:<20} | {data_validade}")
        print("-" * 90)
    else:
        print("Produto não encontrado.")


def atualizar_produto(conn):
    cursor = conn.cursor()
    id_produto = input("Digite o ID do produto que você deseja atualizar: ").strip()
    
    
    p_nome = input("Digite o novo nome do produto a ser cadastrado: ").strip()
    if not p_nome:
        print("O nome do produto é obrigatório.")
        return
    
    
    try:
        p_preco = float(input("Digite o novo preço do produto: "))
        if p_preco < 0:
                print("O preço não pode ser negativo.")
                return
    except ValueError:
        print("Digite um valor numérico válido para o preço.")
        return

    try:
        p_quantidade = int(input("Digite a quantidade do produto: "))
        if p_quantidade < 0:
            print("A quantidade não pode ser negativa.")
            return
    except ValueError:
        print("Digite um número inteiro válido para a quantidade.")
        return
    
    p_descricao = input("Insira a descrição do produto: ").strip() or None

    p_data = input("Digite a data de validade do produto (yyyy-mm-dd): ").strip()
    if not p_data:
        print("A data de validade é obrigatória.")
        return

    cursor.execute("""UPDATE produtos
        SET nome = ?, preco = ?, quantidade = ?, descricao = ?, data_validade = ?
        WHERE id = ?""", (p_nome, p_preco, p_quantidade, p_descricao, p_data, id_produto))
    
    if cursor.rowcount == 0:
        print("ID não encontrado.")
    else:
        conn.commit()
        print("Produto atualizado!")

def deletar_produto(conn):
    cursor = conn.cursor()

    id_produto = input("Digite o ID do produto que deseja excluir: ").strip()

    cursor.execute("SELECT nome FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    if not produto:
        print("ID não encontrado.")
        return
    
    confirmar = input(f"Tem certeza que deseja excluir o produto '{produto[0]}'? (sim/não): ").strip().lower()
    if confirmar != "sim":
        print("Operação cancelada.")
        return
    
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()
    print("Produto excluído!")

#-----------------------------------------main------------------------------------------

def main():
    
    try:
        conn = sqlite3.connect('produtos.db')
        print("Conexão com o banco iniciada.\n")
        executar_script_sql(conn)


        while True:
            print("\n--- MENU ---")
            print("1. Listar produtos")
            print("2. Buscar por ID")
            print("3. Adicionar produto")
            print("4. Atualizar produto")
            print("5. Deletar produto")
            print("6. Sair")

            opcao = input("Escolha: ").strip()

            if opcao == "1":
                exibir_dados(conn)
            elif opcao == "2":
                buscar_por_id(conn)
            elif opcao == "3":
                adicionar_produto(conn)
            elif opcao == "4":
                atualizar_produto(conn)
            elif opcao == "5":
                deletar_produto(conn)
            elif opcao == "6":
                break
            else:
                print("Opção inválida.")


    except sqlite3.Error as error:
        print("Ocorreu um erro -", error)
    finally:
        if conn:
            conn.close()
            print("\nConexão com o banco encerrada.")


if __name__ == "__main__":
    main()