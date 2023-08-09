# Conjuntos em Python não suportam indexação e nem fatiamento
# para acessar o valores é necessario converteo conjunto para a lista.

numeros = {1, 2, 3, 2}

print(numeros[0])

numeros = list(numeros) # comando lista para converter o dados do set em uma lista

print(numeros[0])