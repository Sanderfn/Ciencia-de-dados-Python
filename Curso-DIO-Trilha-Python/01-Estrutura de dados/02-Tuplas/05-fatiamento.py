# Fatiamento -> Permite acessar elementos diretamente e permite extrair um conjunto de valores de uma sequência.
# Para isso deve-se passar o índice inicial e/ou final para acessar o conjunto .
# Podemos ainda informar quantas posições o cursos deve "pular" no acesso.

tupla = ("p", "y", "t", "h","o","n",)

tupla [2:]      # ("t", "h","o","n")
tupla [:2]      # ("p", "y")
tupla [1:3]     # ("y", "t")
tupla [0:3:2]   # ("p", "t")
tupla [::]      # ("p", "y", "t", "h","o","n",)
tupla [::-1]    # ("n","o","h","t","y","p")

print(tupla [2:])
print(tupla [:2])
print(tupla [1:3])
print(tupla [0:3:2])
print(tupla [::])
print(tupla [::-1])