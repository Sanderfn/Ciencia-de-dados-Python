# Listas aninhadas
# Listas aninhadas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas.
# Com Isso podemos criar estruturas bidimensionais(tabelas), e acessar as tabelas informando os ínidces da linha e coluna.
# Exemplo:
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])       # [1, "a", 2]
print(matriz[0][0])    # 1
print(matriz[0][-1])   # 2
print(matriz[-1][-1])  # c
print(matriz[0][2])    # 2  -> (matriz[0][2]) = (matriz[0][-1])