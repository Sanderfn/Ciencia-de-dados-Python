# Enumerate -> Retorna o indice do objeto dentro do laço for. mostrando o indice de cada objeto da lista.

carros =["gol", "celta","palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")
