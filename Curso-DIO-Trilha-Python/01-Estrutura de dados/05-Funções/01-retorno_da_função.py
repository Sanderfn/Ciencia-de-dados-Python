# Return -> Retorna um valor após o usao da palavra reservada return
# Toda função Python retorna NONE por padrão.
# Diferente de outras liguagem de programação, em Python uma função pode retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)