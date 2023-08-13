# Função -> função é um bloco de códiogo idnetificado por um nome e pode receber uma lista de parâmetros.
# Esses parâmetros podem ou não ter valores padrões 
# Usar funções torna o código mais organizado, legivel e reutilizável, permitindo o reaproveitamento do código.
# Programar baseado em funções , é o mesmo que dizer que estamos programando em alto nível e de maneira estruturada.

# def -> definir função

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Antônio"):
    print(f"Seja bem vindo {nome}!")    

exibir_mensagem()
exibir_mensagem_2(nome="Maria")
exibir_mensagem_3()
exibir_mensagem_3(nome="João")