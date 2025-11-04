CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    descricao TEXT,
    data_validade DATE NOT NULL
);

INSERT INTO produtos (nome, preco, quantidade, descricao, data_validade)
VALUES
('Chocolate Amargo', 12.50, 30, 'Barra 70% cacau', '2026-03-01'),
('Biscoito Recheado', 4.75, 50, 'Sabor baunilha', '2025-09-10'),
('Refrigerante Cola', 7.90, 20, 'Garrafa 2L', '2025-07-15'),
('Café Torrado', 18.00, 15, '500g moído', '2026-01-20');