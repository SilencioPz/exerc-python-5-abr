# O Define é identificado por duas variáveis
def dados(nome, idade):
    print(f"{nome} possui {idade} anos.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#O define "imprime" as variáveis no final
dados(nome, idade)