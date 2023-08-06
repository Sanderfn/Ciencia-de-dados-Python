# A compreensão de lista permite cria uma nova lista com base em valores de uma lista existente (tipo um filtro)
# Ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
# append -> adiciona novos valores a uma lista

# Exemplo 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero %2 ==0:
        pares.append(numero)
        print(numero)
        

# Exemplo 2: 

#numeros = [1, 30, 21, 2, 9, 65, 34]
#pares = [numero for numero in numeros if numero % 2 == 0]


# Exemplo 3: Elevando numero ao quadrado

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print()
    print(numero)