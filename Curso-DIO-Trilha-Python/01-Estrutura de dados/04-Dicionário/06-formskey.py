# formkeys -> Cria chaves no dicionários.
#  formkeys -> Cria chaves no dicionários com o mesmo valor de padrão.

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)