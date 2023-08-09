# A função enumerate é utilizada para saber qual o índice do objeto dentro de um laço for.

carros = ("palio", "gol", "celta", "palio")

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")