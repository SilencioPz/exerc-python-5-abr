# Define da soma e média
def calculo(numeros):
    total = sum(numeros)
    
    '''
    Len vem de lenght, comprimento; Neste caso, é calculada a média com base no valor dos números informados.
    '''
    media = total / len(numeros)
    
    return total, media

numeros = [13, 25, 31, 42, 56, 69, 74, 87, 90, 101]

# Calcula a soma e a média
soma, media = calculo(numeros)

print(f"A soma dos números é {soma}.")
print(f"A média dos números é {media}.")