# Objetos de Primeira Classe -> Em Python tudo é objeto e desta forma funções também são objetos.
# Com isso podemos atribuir funções a variáveis, passa-las como parâmetros para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionjários, etc.)
# Usar como valor de retorno para uma função (clouses).

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def teste(a, b):
    return a * 2 + b * 3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é igual a = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 10, teste)  # O resultado da operação 20 + 30 = 50