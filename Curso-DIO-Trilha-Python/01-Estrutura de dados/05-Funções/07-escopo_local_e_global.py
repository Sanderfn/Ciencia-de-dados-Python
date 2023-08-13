# Escopo Local -> localiza-se dentro do bloco onde foi declarado. Portanto as alterações em objetos imutáveis serão perdidas quando o método terminar.
# Escopo Global -> Para usar objetos globais, é necessário declarar a variável com a palavra reservada global antes de declarar. que informa ao interpretador 
# que a variável deve ser usada em todo o programa.
# NÃO É UMA BOA PRATICA E DEVE SER EVITADA

salario = 1000

def salario_bonus(bonus, lista):
    global salario


    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) # 1500
print(salario_com_bonus)
print(lista)   
