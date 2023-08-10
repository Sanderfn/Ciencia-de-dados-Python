# Conjuntos em Python não suportam indexação e nem fatiamento
# para acessar o valores é necessario converteo conjunto para a lista.

numeros = {1, 2, 3, 2}

#print(numeros[0]) # Se o comnetario for retirado e a ação print for chamada, será gerado um erro.

numeros = list(numeros) # comando lista para converter o dados do set em uma lista

print(numeros[0])