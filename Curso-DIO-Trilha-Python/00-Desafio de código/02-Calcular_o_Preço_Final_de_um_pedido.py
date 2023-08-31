
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoFinal = ((valorHamburguer*quantidadeHamburguer)+(valorBebida*quantidadeBebida))

troco = valorPago - precoFinal


print(f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}")


#//TO DO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

#//TO DO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

#//TO DO: Imprimir a saída no formato especificado neste desafio.