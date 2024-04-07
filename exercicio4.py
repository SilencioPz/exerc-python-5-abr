malucos = []

for i in range(5):
    maluco = input("Por favor, digite um nome: ")
    malucos.append(maluco)

indice = int(input("Por favor, informe um número entre 0 e 4: "))

if 0 <= indice <= 4:
    #Pop() remove o que está no indice
    maluco_removido = malucos.pop(indice)
    print("Maluco removido da lista.")
else:
    print("Número entre 0 e 4.")

print(', '.join(malucos))