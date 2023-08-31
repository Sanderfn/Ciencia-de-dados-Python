import textwrap
def menu():
    menu = """\n
    ============== BANCO DIO =============
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    =======================================
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nInsira o dinheiro na maquina")
        print("\nAguarde procesamento da operação!")
        print("\n=== Depósito realizado com sucesso! ===")
        print("\n===================== BANCO DIO ========================")
        print("\n============== COMPROVANTE DE DEPOSITO =================")
        print(f"\nValor do deposito: R$ {valor:.2f}")
        print(f"\nSaldo disponível em conta: R$ {saldo:.2f}")
        print("========================================================")
        print("O Banco DIO agradece por utilizar nossos serviços!")
        
        print("\n Depósito realizado com sucesso! ")

    else:
        print("\n A operação falhou! O valor informado é inválido.")

    return saldo, extrato
 

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou! Você não tem saldo suficiente. ")

    elif excedeu_limite:
        print("\n Operação falhou! O valor do saque excede o limite. ")

    elif excedeu_saques:
        print("\n Operação falhou! Número máximo de saques excedido. ")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1

        print("\n Por favor retire seu dinheiro!")
        print("\nAguarde a emissão de seu comprovante!")
        print("\n==================== BANCO DIO ======================")
        print("\n============== COMPROVANTE DE SAQUE  ================")
        print(f"\nvalor do saque: R$ {valor:.2f}")
        print(f"\nSaldo disponivel para saque: R$ {saldo:.2f}")
        print("=====================================================")
        print("Agradeços por utilizar nossos serviços!")
        print("\n Saque realizado com sucesso! ")

    else:
        print("\n Operação falhou! O valor informado é inválido. ")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe onome do logradouro: ")
    nresidencia = input("Informe o nro da residencia: ")
    complemento = input("Informe o complemento do enedereço: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe a sigla do estado: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "logradouro": logradouro, "nresidencia": nresidencia, "complemento":complemento,
                     "bairro":bairro, "cidade": cidade,"estado":estado })
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n=== Conta criada com sucesso! ===")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()