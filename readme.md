## CRUD de Produtos 🛒

Este projeto é uma aplicação de terminal feita em Python que permite cadastrar, visualizar, atualizar e deletar produtos armazenados em um banco de dados SQLite.

## ⚙️ Recurso Escolhido: Produto

A aplicação trabalha com um único recurso — **Produto**, com as seguintes propriedades:

| Campo          | Tipo de Dado      | Obrigatório | Descrição                                      |
|----------------|------------------|--------------|------------------------------------------------|
| **id**         | INTEGER (PK)      | Sim (auto)   | Identificador único gerado automaticamente     |
| **nome**       | TEXT              | Sim          | Nome do produto                                |
| **preco**      | REAL              | Sim          | Preço unitário do produto                      |
| **quantidade** | INTEGER           | Sim          | Quantidade em estoque                          |
| **descricao**  | TEXT              | Não          | Texto descritivo sobre o produto               |
| **data_validade** | TEXT (YYYY-MM-DD) | Sim        | Data de validade do produto                    |

---

## 🐍 Linguagem

A aplicação foi desenvolvida em **Python 3** utilizando o banco de dados **SQLite**.

## 💻 Instalação e Configuração

1- Clone este repositório:

git clone https://github.com/seu-usuario/crud_produtos.git
cd crud_produtos

2- Execute a aplicação:

python main.py

## 🚀 Como Usar

Após iniciar o programa, o menu exibirá as seguintes opções:

1. Listar produtos
2. Buscar por ID
3. Adicionar produto
4. Atualizar produto
5. Deletar produto
6. Sair

### Exemplo de Uso

**Adicionando um produto:**
<br>Digite o nome do produto a ser cadastrado: Pão Francês
<br>Digite o preço do produto: 0.75
<br>Digite a quantidade do produto: 100
<br>Descrição (opcional): Pão fresco do dia
<br>Digite a data de validade do produto (yyyy-mm-dd): 2025-11-05
<br>Produto adicionado com sucesso!
<br>


**Exemplo — Buscar produto por ID**<br>
Digite o ID do produto que deseja buscar: 3

```
ID  | Nome                     | Preço (R$) | Qtd  | Descrição           | Validade
------------------------------------------------------------------------------------------
3   | Pão Francês              | 0.75       | 100  | Pão fresco do dia   | 2025-11-05
```

### 🧱 Estrutura do Código

O código principal está no arquivo main.py, que contém as seguintes funções:

**criar_tabela(conn):** cria a tabela de produtos no banco SQLite.

**listar_produtos(conn):** lista todos os produtos cadastrados.

**buscar_por_id(conn):** busca e exibe um produto específico.

**adicionar_produto(conn):** adiciona um novo produto ao banco.

**atualizar_produto(conn):** atualiza as informações de um produto existente.

**deletar_produto(conn):** remove um produto do banco de dados.
