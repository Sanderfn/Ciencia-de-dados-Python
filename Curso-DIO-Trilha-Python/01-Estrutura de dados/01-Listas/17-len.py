
linguagens = ["python", "js","c","Java","csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c","js","java","python","csharp"]
# key=lambda x: len(x) -> ordena as palavras em orde, crescente de caracteres(da menor palavra para a maior palavra)
# lambda -> função anonima ("sem nome") no qual o x assume cada argumento da lista, Len(x) retorna o numero de caracteres que cada argumento possui (ex: java = 4 caracteres)

linguagens = ["python", "js","c","Java","csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python","js","java""csharp","c"]
# key=lambda x: len(x) -> ordena as palavras em orde, crescente de caracteres(da menor palavra para a maior palavra)
# lambda -> função anonima ("sem nome") no qual o x assume cada argumento da lista, Len(x) retorna o numero de caracteres que cada argumento possui (ex: java = 4 caracteres)
# reverse -> ordena a inversão do ordem da lista
