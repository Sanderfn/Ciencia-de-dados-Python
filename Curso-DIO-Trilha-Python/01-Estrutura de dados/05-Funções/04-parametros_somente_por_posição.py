# Parametros especiais -> Argumentos podem ser passados para funções que não são obrigatórias.
# Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas 
# olhar para definição para deteminar se os os itens são passados  por posição e nome ou por nome.

def criar_carro (modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# Nesse caso, o parâmetro "marca" é obrigat�)/, marca="Fiat", motor="1.0", combustivel="Gasolina") 
 
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido
