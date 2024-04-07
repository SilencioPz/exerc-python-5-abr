# Defines para cada situação exigida no enunciado
def listinha(lista):
    for nome in lista:
        print(nome)

def nomezim(lista, nome):
    #Atualiza a lista com um novo nome
    lista.append(nome)

def pesquizim(lista, nome):
    if nome in lista:
        print(f"{nome} está na lista.")
    else:
        print(f"{nome} não está na lista.")

nomes = []

for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    #Atualiza a lista vazia com um novo nome
    nomes.append(nome)

print("Lista completa:")
listinha(nomes)

nome = input("Digite um nome para adicionar à lista: ")
nomezim(nomes, nome)

nome = input("Digite um nome para pesquisar na lista: ")
pesquizim(nomes, nome)