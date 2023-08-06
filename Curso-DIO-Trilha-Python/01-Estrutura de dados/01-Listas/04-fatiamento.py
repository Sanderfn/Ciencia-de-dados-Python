# Fatiamento, permite acessar elementos diretamente, extrair um conjunto de valores de uma sequência.
# Para isso basta passar o índice inicial e final para acessar o conjunto.
# Podemos ainda informar quantas posições o cursos deve "pular" no acesso.
lista = ["p","y","t","h","o","n"]

lista[2:]       # ["t","h","o","n"] a lista começa no t pois ele assumi a posição 2, já o : informa que os deamsi caracteres devem ser retornado após o t
lista[:2]       # ["p","y"] O : informa que todos os caracteres tem de ser retornado, já o 2 informa o ultimo caractere a ser retornado antes da posição 2
lista[1:3]      # ["y","t"] O 1 informa a posição que inicia a lista e a posição 3 informa o ultimo caractere a ser retornado antes da posição 3
lista[0:3:2]    # ["p","t"] O 0 informa a posição de inicio da lista. O informa a posição de parada que ´exatamente a posição anteriora informada. O 2 iniforma que a contagem será de dois em dois.
lista[::]       # ["p","y","t","h","o","n"] O : informa que a lista inicia no 1º elemento e o segundo : informa que a lista retornará o ultimo até o último elemento.
lista[::-1]     # ["n","o","h","t","y","p"] O :: informa que irá contemplar todos elementos e o -1 informa que a exibição será invertida.