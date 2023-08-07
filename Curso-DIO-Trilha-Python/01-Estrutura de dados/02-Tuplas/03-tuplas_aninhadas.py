# Tuplas aninhadas -> Tupls podem armazenar todos os tipos de objetos Python.
# Logo Tuplas podem armazenar outras Tuplas, o que pemrite a cração de estruturas bidimensionais (Tabelas).
# As tabelas podem ser e acessadas informando os índices de linha e coluna.

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "C"),
)

matriz[0]      # (1, "a", 2)
matriz[0][0]   # 1
matriz[0][-1]  # 2     
matriz[-1][-1] # "c"

print(matriz[0])     # (1, "a", 2)
print(matriz[0][0])   # 1
print(matriz[0][-1])  # 2     
print(matriz[-1][-1])