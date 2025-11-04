import os
import sqlite3
from main import executar_script_sql, exibir_dados

DB_TESTE = 'teste_produtos.db'

def rodar_testes_completos():
    print("TESTE")
    
    if os.path.exists(DB_TESTE):
        os.remove(DB_TESTE)
        print("Limpando banco de teste antigo...")

    conn_teste = None

    try:
        #Conectar e Criar Tabela
        print("\n[CRIANDO TABELA]")
        conn_teste = sqlite3.connect(DB_TESTE)
        
        executar_script_sql(conn_teste)
        print("Tabela 'produtos' criada E populada com 4 itens.") # <-- Print mais claro
        
        cursor = conn_teste.cursor()

        #Testar INSERT
        print("\n[TESTANDO INSERT]")
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, data_validade) VALUES ('Produto A', 10.0, 5, '2025-01-01')")
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade, data_validade) VALUES ('Produto B', 20.0, 10, '2025-02-02')")
        conn_teste.commit()
        # CORREÇÃO NO PRINT
        print("Produtos 'Produto A' (ID 5) e 'Produto B' (ID 6) inseridos.")
        print("\n Tabela ATUAL após INSERT ")
        exibir_dados(conn_teste)

        #Testar UPDATE
        print("\n[TESTANDO UPDATE]")
        # CORREÇÃO NO PRINT
        print("Atualizando 'Produto A' (ID 5) para 'Produto A (Atualizado)'")
        # CORREÇÃO NO SQL
        cursor.execute("UPDATE produtos SET nome = 'Produto A (Atualizado)', preco = 12.50 WHERE id = 5")
        conn_teste.commit()
        
        
        #Verificação do UPDATE:
        # CORREÇÃO NA VERIFICAÇÃO
        cursor.execute("SELECT nome, preco FROM produtos WHERE id = 5")
        produto_atualizado = cursor.fetchone()
        
        if produto_atualizado and produto_atualizado[0] == 'Produto A (Atualizado)' and produto_atualizado[1] == 12.50:
            # CORREÇÃO NO PRINT
            print("(UPDATE): Produto 5 foi atualizado corretamente.")
        else:
            # CORREÇÃO NO PRINT
            print(f"(UPDATE): Produto 5 não foi atualizado. Encontrado: {produto_atualizado}")
        print("\nTabela ATUAL após UPDATE")
        exibir_dados(conn_teste)

        #Testar DELETE
        print("\n[TESTANDO DELETE]")
        # CORREÇÃO NO PRINT
        print("Deletando 'Produto B' (ID 6)")
        # CORREÇÃO NO SQL
        cursor.execute("DELETE FROM produtos WHERE id = 6")
        conn_teste.commit()
        
        #Verificação do DELETE:
        cursor.execute("SELECT * FROM produtos WHERE id = 6")
        produto_deletado = cursor.fetchone()
        
        if produto_deletado is None:
            # CORREÇÃO NO PRINT
            print("(DELETE): Produto 6 foi deletado corretamente (não foi encontrado).")
        else:
            # CORREÇÃO NO PRINT
            print(f"(DELETE): Produto 6 ainda foi encontrado no banco.")
            
        # Adicionando a exibição final para ver o resultado do DELETE
        print("\nTabela ATUAL após DELETE")
        exibir_dados(conn_teste)

    except sqlite3.Error as e:
        print(f"FALHA GERAL: Um erro de SQL ocorreu durante os testes. Erro: {e}")
    
    finally:
        if conn_teste:
            conn_teste.close()
        if os.path.exists(DB_TESTE):
            os.remove(DB_TESTE)
            print("\nBanco de teste limpo. Teste finalizado.") # <-- Print final

if __name__ == "__main__":
    rodar_testes_completos()