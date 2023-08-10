# Os dados são acessados e modificados através da chave.
dados ={"nome": "guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]       # "Guilherme"
dados["idade"]      # "28"
dados["telefone"]   # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "998-1781"

dados # {"nome": "Maria", "idade":18, "telefone":"998-1781"}