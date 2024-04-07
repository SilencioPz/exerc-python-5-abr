def imprimindoMenu():
    print("1 - Hello World")
    print("2 - Início da programação em Python")
    print("3 - Modularização com Python")

def escolhendo(escolha):
    if escolha == 1:
        print("Hello World")
    elif escolha == 2:
        print("Início da programação em Python")
    elif escolha == 3:
        print("Modularização com Python")
    else:
        print("Erro. Favor, escolha uma opção válida.")

while True:
    imprimindoMenu()
    escolha = int(input("Escolha uma opção: "))
    escolhendo(escolha)
    if 1 <= escolha <= 3:
        break