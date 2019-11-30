class Dados_bancarios:
    def __init__(self, nome, idade, saque, deposito, emprestimo, visualizar_informacoes):
        self. nome = nome
        self. idade = idade
        self. saque = saque
        self. deposito = deposito
        self. emprestimo = emprestimo
        self. visualizar_informacoes = visualizar_informacoes

dados_bancarios = Dados_bancarios(
    nome = input("Digite seu nome completo"),
    idade = int(input("Digite a idade")),
    saque = float(input("Digite o valor do saque")),
    deposito = float(input("Digite o valor do depósito")),
    emprestimo = float(input("Digite o valor do empréstimo")),
    visualizar_informacoes = Dados_bancarios
)

print(dados_bancarios)




