#estruturas condicionais permitem o desvio de fluxo de controle quando um condição é atendida
#IF = Cria uma estrutura condicional simples por um unico desvio.
# exemplo:

saldo = 2000.00
saque = float(input("Informe o valor que deseja sacar: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")
