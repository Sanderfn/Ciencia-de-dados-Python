menu = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair
 => """

saldo = 0
limite = 1000
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3 # Este valor é uma constante


while True:

    opcao = input(menu)
 
    if opcao == "d":
        print("\nVocê selecionou a opcao depósitar!")
        valor = float(input("\nInforme o valor que deseja depositar:"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

            print("\n Insira o dinheiro na maquina")
            print("\nAguarde procesamento da operação!")
            print("\n============== COMPROVANTE DE DEPOSITO  ================")
            print(f"\nvalor do deposito: R$ {valor:.2f}")
            print(f"\nSaldo disponível em conta: R$ {saldo:.2f}")
            print("========================================================")
            print("Agradeços por utilizar nossos serviços!")

        else:
            print("operação falhou! o valor informado é invalido.")
            
    elif opcao == "s":

        print("\nVocê selecionou a opcao Sacar!")

        valor = float(input("\nInforme o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
     
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor de saque excede o limite.")

        elif excedeu_saque:
            print("\nOperação falhou! Número máximo de 4 saques diario foi excedido.")

        elif valor > 0:
            saldo -=valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

            print("\n Por favor retire seu dinheiro!")
            print("\nAguarde a emissão de seu comprovante!")
            print("\n============== COMPROVANTE DE SAQUE  ================")
            print(f"\nvalor do saque: R$ {valor:.2f}")
            print(f"\nSaldo disponivel para saque: R$ {saldo:.2f}")
            print("=====================================================")
            print("Agradeços por utilizar nossos serviços!")

        else:
            print("Operação falhou! O valor informado é invalido.")
  

    elif opcao == "e":

        print("\nVocê selecionou a opcao extrato!")
        print("\nAguarde enquanto carregamos sua informações!")
        print("\n==============  EXTRATO  ================")
        print("Não Foram realziadas movimentações." if not extrato else extrato)
        print(f"\nSaldo disponível: R$ {saldo:.2f}")
        print("=========================================")
        print("Agradeços por utilizar nossos serviços!")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")