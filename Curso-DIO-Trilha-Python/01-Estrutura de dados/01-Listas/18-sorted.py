# sorted -> trata-se dum função built

linguagens = ["python", "js","c","Java","csharp"]
sorted(linguagens, key=lambda x:len(x)) # ["c","js","java","python","csharp"]
# srted -> por ser uma função deve-se passa o iterável para função.
print(sorted(linguagens))

linguagens = ["python", "js","c","Java","csharp"]
sorted(linguagens, key=lambda x:len(x),  reverse=True) # ["c","js","java","python","csharp"]
